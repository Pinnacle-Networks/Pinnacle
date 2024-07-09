from ibis.backends import BaseBackend
from pymongo import MongoClient

from pinnacle.backends.ibis.data_backend import IbisDataBackend
from pinnacle.backends.local.artifacts import FileSystemArtifactStore
from pinnacle.backends.mongodb.artifacts import MongoArtifactStore
from pinnacle.backends.mongodb.data_backend import MongoDataBackend
from pinnacle.backends.mongodb.metadata import MongoMetaDataStore
from pinnacle.backends.sqlalchemy.metadata import SQLAlchemyMetadata
from pinnacle.vector_search.atlas import MongoAtlasVectorSearcher
from pinnacle.vector_search.in_memory import InMemoryVectorSearcher
from pinnacle.vector_search.lance import LanceVectorSearcher

data_backends = {
    'mongodb': MongoDataBackend,
    'ibis': IbisDataBackend,
}

artifact_stores = {
    'mongodb': MongoArtifactStore,
    'filesystem': FileSystemArtifactStore,
}

metadata_stores = {
    'mongodb': MongoMetaDataStore,
    'sqlalchemy': SQLAlchemyMetadata,
}

vector_searcher_implementations = {
    'lance': LanceVectorSearcher,
    'in_memory': InMemoryVectorSearcher,
    'mongodb+srv': MongoAtlasVectorSearcher,
}

CONNECTIONS = {
    'pymongo': MongoClient,
    'ibis': BaseBackend,
}
