import os

import pytest

from pinnacledb.misc import pinnacle

SDDB_USE_MONGOMOCK = 'SDDB_USE_MONGOMOCK' in os.environ


@pytest.fixture(autouse=SDDB_USE_MONGOMOCK)
def patch_mongomock(monkeypatch):
    import gridfs
    import gridfs.grid_file
    import pymongo
    from mongomock import Collection, Database, MongoClient

    from pinnacledb.db.base.backends import CONNECTIONS

    monkeypatch.setattr(gridfs, 'Collection', Collection)
    monkeypatch.setattr(gridfs.grid_file, 'Collection', Collection)
    monkeypatch.setattr(gridfs, 'Database', Database)
    monkeypatch.setattr(pinnacle, 'Database', Database)
    monkeypatch.setattr(pymongo, 'MongoClient', MongoClient)

    monkeypatch.setitem(CONNECTIONS, 'pymongo', MongoClient)
