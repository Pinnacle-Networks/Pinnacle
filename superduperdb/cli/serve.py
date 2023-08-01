import typing as t

import pinnacledb as s

from . import command


@command(help='Start server')
def serve():
    from pinnacledb.db.base.build import build_datalayer
    from pinnacledb.server.server import serve

    db = build_datalayer()
    serve(db)


@command(help='Start local cluster: server, dask and change data capture')
def local_cluster(on: t.List[str] = []):
    from pinnacledb.db.base.build import build_datalayer
    from pinnacledb.db.base.cdc import DatabaseListener
    from pinnacledb.db.mongodb.query import Collection
    from pinnacledb.server.dask_client import dask_client
    from pinnacledb.server.server import serve

    db = build_datalayer()
    dask_client(s.CFG.dask, local=True)
    for collection in on:
        w = DatabaseListener(
            db=db,
            on=Collection(name=collection),
        )
        w.listen()
    serve(db)
