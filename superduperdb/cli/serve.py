import typing as t

from pinnacledb import CFG
from pinnacledb.cluster.dask_client import dask_client
from pinnacledb.cluster.server import serve as _serve
from pinnacledb.datalayer.base.build import build_datalayer
from pinnacledb.datalayer.base.cdc import DatabaseWatcher
from pinnacledb.datalayer.mongodb.query import Collection

from . import command


@command(help='Start server')
def serve():
    db = build_datalayer()
    _serve(db)


@command(help='Start local cluster: server, dask and change data capture')
def local_cluster(on: t.Sequence[str] = []):
    db = build_datalayer()
    dask_client(CFG.dask, local=True)
    for collection in on:
        w = DatabaseWatcher(
            db=db,
            on=Collection(name=collection),
        )
        w.watch()
    _serve(db)
