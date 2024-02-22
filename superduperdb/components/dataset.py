from __future__ import annotations

import dataclasses as dc
import typing as t
from functools import cached_property

import numpy
from overrides import override

from pinnacledb.backends.mongodb.query import Select
from pinnacledb.base.datalayer import Datalayer
from pinnacledb.base.document import Document
from pinnacledb.components.component import Component, ensure_initialized
from pinnacledb.components.datatype import (
    DataType,
    dill_serializer,
    pickle_decode,
    pickle_encode,
)
from pinnacledb.misc.annotations import public_api


@public_api(stability='stable')
@dc.dataclass(kw_only=True)
class Dataset(Component):
    """A dataset is an immutable collection of documents.
    {component_params}
    :param select: A query to select the documents for the dataset
    :param sample_size: The number of documents to sample from the query
    :param random_seed: The random seed to use for sampling
    :param creation_date: The date the dataset was created
    :param raw_data: The raw data for the dataset
    """

    __doc__ = __doc__.format(component_params=Component.__doc__)

    type_id: t.ClassVar[str] = 'dataset'
    _artifacts: t.ClassVar[t.Sequence[t.Tuple[str, DataType]]] = (
        ('raw_data', dill_serializer),
    )

    select: t.Optional[Select] = None
    sample_size: t.Optional[int] = None
    random_seed: t.Optional[int] = None
    creation_date: t.Optional[str] = None
    raw_data: t.Optional[t.Sequence[t.Any]] = None

    def __post_init__(self, artifacts):
        self._data = None
        return super().__post_init__(artifacts)

    @property
    @ensure_initialized
    def data(self):
        return self._data

    def init(self):
        super().init()
        self._data = [Document.decode(r, self.db) for r in pickle_decode(self.raw_data)]

    @override
    def pre_create(self, db: 'Datalayer') -> None:
        if self.raw_data is None:
            if self.select is None:
                raise ValueError('select cannot be None')
            data = list(db.execute(self.select))
            if self.sample_size is not None and self.sample_size < len(data):
                perm = self.random.permutation(len(data)).tolist()
                data = [data[perm[i]] for i in range(self.sample_size)]
            self.raw_data = pickle_encode([r.encode() for r in data])

    @cached_property
    def random(self):
        return numpy.random.default_rng(seed=self.random_seed)
