import re
import typing as t

from pinnacle.base.configs import CFG

__all__ = ('pinnacle',)


def pinnacle(item: str | None = None, **kwargs) -> t.Any:
    """Build a pinnacle connection.

    :param item: URI of connection.
    :param kwargs: Additional parameters to building `Datalayer`
    """
    from pinnacle.base.build import build_datalayer

    if item is None:
        return build_datalayer()

    if item.startswith('mongomock://'):
        kwargs['data_backend'] = item

    elif item.startswith('mongodb://'):
        kwargs['data_backend'] = item

    elif item.startswith('mongodb+srv://') and 'mongodb.net' in item:
        kwargs['data_backend'] = item

    elif item.endswith('.csv'):
        if CFG.cluster.cdc.uri is not None:
            raise TypeError('Pandas is not supported in cluster mode!')
        kwargs['data_backend'] = item

    else:
        if re.match(r'^[a-zA-Z0-9]+://', item) is None:
            raise ValueError(f'{item} is not a valid connection string')
        kwargs['data_backend'] = item
    return build_datalayer(CFG, **kwargs)
