from pymongo import MongoClient

from pinnacledb.base import config
from pinnacledb.db.mongodb.artifacts import MongoArtifactStore
from pinnacledb.db.mongodb.data_backend import MongoDataBackend
from pinnacledb.db.mongodb.metadata import MongoMetaDataStore
from pinnacledb.vector_search.inmemory import InMemoryVectorDatabase
from pinnacledb.vector_search.lancedb_client import LanceVectorIndex

data_backends = {'mongodb': MongoDataBackend}

artifact_stores = {'mongodb': MongoArtifactStore}

metadata_stores = {'mongodb': MongoMetaDataStore}

vector_database_stores = {
    config.LanceDB: LanceVectorIndex,
    config.InMemory: InMemoryVectorDatabase,
}

connections = {
    'pymongo': MongoClient,
}
