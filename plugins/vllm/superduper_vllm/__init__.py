from pinnacle.ext.vllm.model import VllmAPI, VllmModel
from pinnacle.misc.annotations import requires_packages

__all__ = ["VllmAPI", "VllmModel"]

_, requirements = requires_packages(
    ['vllm', None, None], ['ray', None, None], warn=True
)
