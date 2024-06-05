from pinnacledb import Component, pinnacle

from . import command


@command(help='Apply the stack tarball to the database')
def apply(path: str):
    """Apply a serialized component.

    :param path: Path to the stack.
    """
    db = pinnacle()
    component = Component.read(path)
    db.apply(component)
