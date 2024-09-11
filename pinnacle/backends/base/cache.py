from abc import abstractmethod, ABC

from pinnacle.backends.base.backends import BaseBackend
from pinnacle.components.component import Component


class Cache(BaseBackend):
    """Cache object for caching components.
    
    # noqa
    """

    @abstractmethod
    def __getitem__(self, *item) -> Component:
        """Get a component from the cache."""
        pass
