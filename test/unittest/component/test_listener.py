from pinnacledb.backends.mongodb.query import Collection
from pinnacledb.components.listener import Listener
from pinnacledb.components.model import Model


def test_listener_serializes_properly():
    q = Collection('test').find({}, {})
    listener = Listener(
        model=Model('test', object=lambda x: x),
        select=q,
        key='test',
    )
    r = listener.dict().encode()

    # check that the result is JSON-able
    import json

    print(json.dumps(r, indent=2))
