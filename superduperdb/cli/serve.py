import typing as t

from pinnacledb import CFG
from pinnacledb.db.base.build import build_datalayer
from pinnacledb.db.base.cdc import DatabaseWatcher
from pinnacledb.db.mongodb.query import Collection
from pinnacledb.server.dask_client import dask_client
from pinnacledb.server.server import serve as _serve

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
