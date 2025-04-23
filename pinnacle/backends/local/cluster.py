from pinnacle.backends.base.cluster import Cluster
from pinnacle.backends.local.cdc import LocalCDCBackend
from pinnacle.backends.local.compute import LocalComputeBackend
from pinnacle.backends.local.crontab import LocalCrontabBackend
from pinnacle.backends.local.scheduler import LocalScheduler
from pinnacle.backends.local.vector_search import LocalVectorSearchBackend
from pinnacle.base.exceptions import InvalidArguments
from pinnacle.misc.importing import load_plugin


class LocalCluster(Cluster):
    """Local cluster for running infra locally."""

    @classmethod
    def build(cls, CFG, **kwargs):
        """Build the local cluster."""
        # the build function must carry a DB object.
        # FIXME: make this argument explicit
        db = kwargs.get('db', None)
        if db is None:
            raise InvalidArguments("The 'db' parameter is required in kwargs")

        # extract custom implementations
        searcher_impl = load_plugin(CFG.vector_search_engine).VectorSearcher

        cluster = LocalCluster(
            scheduler=LocalScheduler(db=db),
            compute=LocalComputeBackend(db=db),
            vector_search=LocalVectorSearchBackend(db=db, searcher_impl=searcher_impl),
            cdc=LocalCDCBackend(db=db),
            crontab=LocalCrontabBackend(db=db),
        )

        return cluster
