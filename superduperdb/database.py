from pymongo.database import Database as BaseDatabase
import pinnacledb.collection


class Database(BaseDatabase):
    """
    Database building on top of :code:`pymongo.database.Database`. Collections in the
    database are SuperDuperDB objects :code:`pinnacledb.collection.Collection`.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __getitem__(self, name: str):
        return pinnacledb.collection.Collection(self, name)
