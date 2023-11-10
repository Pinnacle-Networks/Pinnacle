import typing as t

import pinnacledb as s

from . import command


@command(help='Start server')
def serve():
    from pinnacledb.base.build import build_datalayer
    from pinnacledb.server.server import serve

    db = build_datalayer()
    serve(db)


@command(help='Start local dask cluster')
def local_dask():
    raise NotImplementedError


@command(help='Start local cluster: server, dask and change data capture')
def local_cluster(on: t.List[str] = []):
    from pinnacledb.backends.mongodb.query import Collection
    from pinnacledb.base.build import build_datalayer
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


@command(help='Start vector search server')
def vector_search():
    from pinnacledb.vector_search.server.app import app

    app.start()


@command(help='Start standalone change data capture')
def cdc():
    from pinnacledb.cdc.app import app

    app.start()
