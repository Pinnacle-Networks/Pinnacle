from .base import config, configs, jsonable, logger
from .misc.pinnacle import pinnacle

__all__ = 'CFG', 'ICON', 'JSONable', 'ROOT', 'config', 'log', 'logging', 'pinnacle'

ICON = '🔮'
CFG = configs.CFG
JSONable = jsonable.JSONable
ROOT = configs.ROOT

logging = log = logger.logging

__version__ = '0.0.7'
