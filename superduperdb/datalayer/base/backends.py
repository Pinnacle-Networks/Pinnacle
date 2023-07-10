from pymongo import MongoClient

from pinnacledb.datalayer.mongodb.artifacts import MongoArtifactStore
from pinnacledb.datalayer.mongodb.data_backend import MongoDataBackend
from pinnacledb.datalayer.mongodb.metadata import MongoMetaDataStore
from pinnacledb.vector_search.inmemory import InMemoryVectorDatabase
from pinnacledb.vector_search.lancedb_client import LanceVectorIndex
from pinnacledb.misc import config


data_backends = {'mongodb': MongoDataBackend}

artifact_stores = {'mongodb': MongoArtifactStore}

metadata_stores = {'mongodb': MongoMetaDataStore}

vector_database_stores = {
    config.LanceDB: LanceVectorIndex,  # type: ignore [dict-item]
    config.InMemory: InMemoryVectorDatabase,  # type: ignore [dict-item]
}

connections = {
    'pymongo': MongoClient,
}
