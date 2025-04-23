import typing as t

import click
import numpy

from pinnacle import logging
from pinnacle.backends.base.cluster import Cluster
from pinnacle.backends.base.vector_search import (
    BaseVectorSearcher,
    VectorItem,
    measures,
)
from pinnacle.backends.local.cache import LocalCache
from pinnacle.backends.local.cdc import LocalCDCBackend
from pinnacle.backends.local.compute import LocalComputeBackend
from pinnacle.backends.local.crontab import LocalCrontabBackend
from pinnacle.backends.local.scheduler import LocalScheduler
from pinnacle.backends.local.vector_search import LocalVectorSearchBackend
from pinnacle.misc.importing import load_plugin


class LocalCluster(Cluster):
    """Local cluster for running infra locally.

    :param compute: The compute backend.
    :param cache: The cache backend.
    :param scheduler: The scheduler backend.
    :param vector_search: The vector search backend.
    :param cdc: The change data capture backend.
    :param crontab: The crontab backend.
    """

    @classmethod
    def build(cls, CFG, **kwargs):
        """Build the local cluster."""
        searcher_impl = load_plugin(CFG.vector_search_engine).VectorSearcher
        cache = None
        if CFG.cache and CFG.cache.startswith('redis'):
            cache = load_plugin('redis').Cache(uri=CFG.cache)
        elif CFG.cache:
            assert CFG.cache == 'in-process'
            cache = LocalCache()

        return LocalCluster(
            cache=cache,
            scheduler=LocalScheduler(),
            compute=LocalComputeBackend(),
            vector_search=LocalVectorSearchBackend(searcher_impl=searcher_impl),
            cdc=LocalCDCBackend(),
            crontab=LocalCrontabBackend(),
        )

    def drop(self, force: bool = False):
        """Drop the cluster.

        :param force: Force drop the cluster.
        """
        if not force:
            if not click.confirm(
                "Are you sure you want to drop the cache? ",
                default=False,
            ):
                logging.warn("Aborting...")
        if self.cache is not None:
            return self.cache.drop()
