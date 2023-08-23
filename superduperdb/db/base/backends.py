from pymongo import MongoClient
from ibis.backends.base import BaseBackend

from pinnacledb.base import config
from pinnacledb.db.mongodb.artifacts import MongoArtifactStore
from pinnacledb.db.mongodb.data_backend import MongoDataBackend
from pinnacledb.db.filesystem.artifacts import FileSystemArtifactStore
from pinnacledb.db.sqlalchemy.metadata import  SQLAlchemyMetadata
from pinnacledb.db.ibis.data_backend import IbisDataBackend
from pinnacledb.db.mongodb.metadata import MongoMetaDataStore
from pinnacledb.vector_search.inmemory import InMemoryVectorDatabase
from pinnacledb.vector_search.lancedb_client import LanceVectorIndex

data_backends = {'mongodb': MongoDataBackend, 'ibis': IbisDataBackend}

artifact_stores = {'mongodb': MongoArtifactStore, 'filesystem': FileSystemArtifactStore}

metadata_stores = {'mongodb': MongoMetaDataStore, 'sqlalchemy': SQLAlchemyMetadata}

VECTOR_DATA_STORES = {
    config.LanceDB: LanceVectorIndex,
    config.InMemory: InMemoryVectorDatabase,
}

CONNECTIONS = {
    'pymongo': MongoClient,
    'ibis': BaseBackend,
}
