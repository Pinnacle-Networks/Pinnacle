import typing as t
from abc import ABC, abstractmethod

from pinnacledb.container.document import Document
from pinnacledb.container.model import Model
from pinnacledb.db.base.query import Select


class BaseDataBackend(ABC):
    models: t.Dict[str, Model]
    select_cls = Select
    id_field = 'id'

    def __init__(self, conn: t.Any, name: str):
        self.conn = conn
        self.name = name

    @property
    def db(self):
        raise NotImplementedError

    @abstractmethod
    def drop(self, force=False):
        """
        Drop the databackend.
        """
        pass

    @abstractmethod
    def get_output_from_document(self, r: Document, key: str, model: str):
        pass

    @abstractmethod
    def set_content_bytes(self, r, key, bytes_):
        pass

    @abstractmethod
    def unset_outputs(self, info):
        pass
