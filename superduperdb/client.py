from pymongo.mongo_client import MongoClient

import pinnacledb.database
from pinnacledb import cf


class SuperDuperClient(MongoClient):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.args = args
        self.kwargs = kwargs

    def __getitem__(self, name: str):
        return pinnacledb.database.Database(self, name)


the_client = SuperDuperClient(**cf['mongodb'])