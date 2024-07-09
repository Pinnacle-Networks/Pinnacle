from pinnacle import Component, logging, pinnacle

from . import command


@command(help='Apply the component to a `pinnacle` deployment')
def apply(path: str):
    """Apply a serialized component.

    :param path: Path to the stack.
    """
    _apply(path)


@command(help='`pinnacle` deployment')
def drop(data: bool = False, force: bool = False):
    """Apply a serialized component.

    :param path: Path to the stack.
    """
    db = pinnacle()
    db.drop(force=force, data=data)
    db.disconnect()


def _apply(path: str):
    try:
        logging.info('Connecting to pinnacle')
        db = pinnacle()
        logging.info('Reading component')
        component = Component.read(path)
        logging.info('Applying component to pinnacle')
        db.apply(component)
    except Exception as e:
        raise e
    finally:
        db.disconnect()
