from dask.distributed import Client
from pinnacledb import CFG


def dask_client():
    return Client(
        address=f'tcp://{CFG.dask.ip}:{CFG.dask.port}',
        serializers=CFG.dask.serializers,
        deserializers=CFG.dask.deserializers,
    )
