import importlib

from pinnacle import logging


def load_plugin(name: str):
    """Load a plugin by name.

    :param name: The name of the plugin to load.
    """
    if name == 'local':
        return importlib.import_module('pinnacle.backends.local')
    logging.info(f"Loading plugin: {name}")
    plugin = importlib.import_module(f'pinnacle_{name}')
    return plugin


def import_object(path):
    """Import item from path.

    :param path: Path to import from.
    """
    module = '.'.join(path.split('.')[:-1])
    cls = path.split('.')[-1]
    return getattr(importlib.import_module(module), cls)
