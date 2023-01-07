from pymongo.database import Database as BaseDatabase
import pinnacledb.collection


class Database(BaseDatabase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __getitem__(self, name: str):
        return pinnacledb.collection.Collection(self, name)
