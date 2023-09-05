from ibis.backends.base import BaseBackend
from pymongo import MongoClient

from pinnacledb.db.filesystem.artifacts import FileSystemArtifactStore
from pinnacledb.db.ibis.data_backend import IbisDataBackend
from pinnacledb.db.mongodb.artifacts import MongoArtifactStore
from pinnacledb.db.mongodb.data_backend import MongoDataBackend
from pinnacledb.db.mongodb.metadata import MongoMetaDataStore
from pinnacledb.db.sqlalchemy.metadata import SQLAlchemyMetadata
from pinnacledb.vector_search.inmemory import InMemoryVectorDatabase
from pinnacledb.vector_search.lancedb_client import LanceVectorIndex

data_backends = {'mongodb': MongoDataBackend, 'ibis': IbisDataBackend}

artifact_stores = {'mongodb': MongoArtifactStore, 'filesystem': FileSystemArtifactStore}

metadata_stores = {'mongodb': MongoMetaDataStore, 'sqlalchemy': SQLAlchemyMetadata}

vector_data_stores = {
    'lancedb': LanceVectorIndex,
    'inmemory': InMemoryVectorDatabase,
}

CONNECTIONS = {
    'pymongo': MongoClient,
    'ibis': BaseBackend,
    'lancedb': LanceVectorIndex,
    'inmemory': InMemoryVectorDatabase,
}
