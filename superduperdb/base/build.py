import re
import sys

import ibis
import mongomock
import pymongo

import pinnacledb as s
from pinnacledb import logging
from pinnacledb.backends.base.backends import data_backends, metadata_stores
from pinnacledb.backends.filesystem.artifacts import FileSystemArtifactStore
from pinnacledb.backends.mongodb.artifacts import MongoArtifactStore
from pinnacledb.base.datalayer import Datalayer
from pinnacledb.server.dask_client import dask_client


def build_artifact_store(cfg):
    if cfg.artifact_store is None:
        raise ValueError('No artifact store specified')
    elif cfg.artifact_store.startswith('mongodb://'):
        import pymongo

        conn = pymongo.MongoClient('/'.join(cfg.artifact_store.split('/')[:-1]))
        name = cfg.artifact_store.split('/')[-1]
        return MongoArtifactStore(conn, name)
    elif cfg.artifact_store.startswith('filesystem://'):
        directory = cfg.artifact_store.split('://')[1]
        return FileSystemArtifactStore(directory)
    else:
        raise ValueError(f'Unknown artifact store: {cfg.artifact_store}')


def build_datalayer(cfg=None, **kwargs) -> Datalayer:
    """
    Build a Datalayer object as per ``db = pinnacle(db)`` from configuration.

    :param cfg: Configuration to use. If None, use ``pinnacledb.CFG``.
    """

    # Use the provided configuration or fall back to the default configuration.
    cfg = cfg or s.CFG

    # Update configuration with keyword arguments.
    for k, v in kwargs.items():
        cfg.force_set(k, v)

    # Helper function to build a data backend based on the URI.
    def build(uri, mapping):
        logging.debug(f"Parsing data connection URI:{uri}")

        if re.match('^mongodb:\/\/|^mongodb\+srv:\/\/', uri) is not None:
            name = uri.split('/')[-1]
            conn = pymongo.MongoClient(
                uri,
                serverSelectionTimeoutMS=5000,
            )

            return mapping['mongodb'](conn, name)
        elif uri.startswith('mongomock://'):
            name = uri.split('/')[-1]
            conn = mongomock.MongoClient()
            return mapping['mongodb'](conn, name)
        else:
            name = uri.split('//')[0]
            conn = ibis.connect(uri)
            return mapping['ibis'](conn, name)

    # Connect to data backend.
    try:
        databackend = build(cfg.data_backend, data_backends)
        logging.info("Data Client is ready.", databackend.conn)
    except Exception as e:
        # Exit quickly if a connection fails.
        logging.error("Error initializing to DataBackend Client:", str(e))
        sys.exit(1)

    # Build a Datalayer object with the specified components.
    db = Datalayer(
        databackend=databackend,
        metadata=(
            build(cfg.metadata_store, metadata_stores)
            if cfg.metadata_store is not None
            else databackend.build_metadata()
        ),
        artifact_store=(
            build_artifact_store(cfg)
            if cfg.artifact_store is not None
            else databackend.build_artifact_store()
        ),
        distributed_client=dask_client(
            cfg.cluster.dask_scheduler,
            local=cfg.cluster.local,
            serializers=cfg.cluster.serializers,
            deserializers=cfg.cluster.deserializers,
        )
        if cfg.mode == 'production'
        else None,
    )

    return db
