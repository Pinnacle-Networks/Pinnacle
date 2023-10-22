from ibis.backends.base import BaseBackend
from pymongo import MongoClient

from pinnacledb.db.filesystem.artifacts import FileSystemArtifactStore
from pinnacledb.db.ibis.data_backend import IbisDataBackend
from pinnacledb.db.mongodb.artifacts import MongoArtifactStore
from pinnacledb.db.mongodb.data_backend import MongoDataBackend
from pinnacledb.db.mongodb.metadata import MongoMetaDataStore
from pinnacledb.db.sqlalchemy.metadata import SQLAlchemyMetadata
from pinnacledb.vector_search.in_memory import InMemoryVectorSearcher
from pinnacledb.vector_search.lance import LanceVectorSearcher

data_backends = {'mongodb': MongoDataBackend, 'ibis': IbisDataBackend}

artifact_stores = {'mongodb': MongoArtifactStore, 'filesystem': FileSystemArtifactStore}

metadata_stores = {'mongodb': MongoMetaDataStore, 'sqlalchemy': SQLAlchemyMetadata}

vector_searcher_implementations = {
    'lance': LanceVectorSearcher,
    'in_memory': InMemoryVectorSearcher,
}

CONNECTIONS = {
    'pymongo': MongoClient,
    'ibis': BaseBackend,
}
