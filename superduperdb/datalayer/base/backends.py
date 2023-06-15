from pymongo import MongoClient

from pinnacledb.datalayer.mongodb.artifacts import MongoArtifactStore
from pinnacledb.datalayer.mongodb.data_backend import MongoDataBackend
from pinnacledb.datalayer.mongodb.metadata import MongoMetaDataStore


data_backends = {'mongodb': MongoDataBackend}

artifact_stores = {'mongodb': MongoArtifactStore}

metadata_stores = {'mongodb': MongoMetaDataStore}

connections = {
    'pymongo': MongoClient,
}
