from . import command
from pinnacledb.server.server import Server
from tests.unittests.server.test_server import Object


@command(help='Start server')
def serve():
    Server().auto_run(Object())
