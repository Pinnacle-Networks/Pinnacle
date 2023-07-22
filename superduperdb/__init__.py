from .misc import config, configs
from .misc.jsonable import JSONable

__all__ = 'CFG', 'ICON', 'JSONable', 'ROOT', 'config', 'log', 'logging', 'pinnacle'

ICON = '🔮'
CFG = configs.CFG
ROOT = configs.ROOT

from .misc import logger  # noqa: E402
from .misc.pinnacle import pinnacle  # noqa: E402

log = logger.logging

__version__ = '0.0.0'  # overwritten by build system on GH Actions
