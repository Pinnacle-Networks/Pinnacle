from pinnacledb.base.build import build_datalayer
from pinnacledb.components.stack import Stack

from . import command


@command(help='Apply the stack tarball to the database')
def apply(yaml_path: str, identifier: str):
    db = build_datalayer()
    stack = Stack(identifier=identifier)
    stack.load(yaml_path)
    db.add(stack)
