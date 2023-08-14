import typing as t

from pinnacledb import logging
from pinnacledb.container.document import Document
from pinnacledb.container.serializable import Serializable
from pinnacledb.db.base.data_backend import BaseDataBackend
from pinnacledb.misc.special_dicts import MongoStyleDict


class IbisDataBackend(BaseDataBackend):
    id_field = 'id'

    def __init__(self, conn, name: str):
        super().__init__(conn=conn, name=name)
        # Get database.
        self._db = self.conn[self.name]

    @property
    def db(self):
        return self._db
