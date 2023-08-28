from pymongo import MongoClient

from pinnacledb.base import config
from pinnacledb.db.mongodb.artifacts import MongoArtifactStore
from pinnacledb.db.mongodb.data_backend import MongoDataBackend
from pinnacledb.db.mongodb.metadata import MongoMetaDataStore
from pinnacledb.vector_search.inmemory import InMemoryVectorDatabase
from pinnacledb.vector_search.lancedb_client import LanceVectorIndex

DATA_BACKENDS = {'mongodb': MongoDataBackend}

ARTIFACT_STORES = {'mongodb': MongoArtifactStore}

METADATA_STORES = {'mongodb': MongoMetaDataStore}

VECTOR_DATA_STORES = {
    config.LanceDB: LanceVectorIndex,
    config.InMemory: InMemoryVectorDatabase,
}

CONNECTIONS = {
    'pymongo': MongoClient,
}
