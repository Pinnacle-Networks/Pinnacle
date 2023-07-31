from .base import config, configs, jsonable, logger

__all__ = 'CFG', 'ICON', 'JSONable', 'ROOT', 'config', 'log', 'logging', 'pinnacle'

ICON = '🔮'
CFG = configs.CFG
JSONable = jsonable.JSONable
ROOT = configs.ROOT

from .misc.pinnacle import pinnacle  # noqa: E402

logging = log = logger.logging

__version__ = '0.0.0'  # overwritten by build system on GH Actions
