from pinnacledb.ext.vllm.model import VllmAPI, VllmModel
from pinnacledb.misc.annotations import requires_packages

__all__ = ["VllmAPI", "VllmModel"]

requires_packages(['vllm', None, None], ['ray', None, None], warn=True)
