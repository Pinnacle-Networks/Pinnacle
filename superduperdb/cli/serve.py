import typing as t

import pinnacledb as s

from . import command


@command(help='Start server')
def serve():
    from pinnacledb.base.build import build_datalayer
    from pinnacledb.server.server import serve

    db = build_datalayer()
    serve(db)


@command(help='Start local cluster: server, dask and change data capture')
def local_cluster(on: t.List[str] = []):
    from pinnacledb.base.build import build_datalayer
    from pinnacledb.db.mongodb.query import Collection
    from pinnacledb.server.dask_client import dask_client
    from pinnacledb.server.server import serve

    db = build_datalayer()
    dask_client(
        uri=s.CFG.cluster.dask_scheduler,
        local=True,
    )
    for collection in on:
        db.cdc.listen(
            on=Collection(identifier=collection),
        )
    serve(db)
