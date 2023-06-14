import importlib
import pinnacledb as s
import typing as t


def get_database_from_database_type(database_type: str, database_name: str) -> t.Any:
    """
    Import the database connection from ``pinnacledb``

    :param database_type: type of database (supported: ['mongodb'])
    :param database_name: name of database
    """
    module = importlib.import_module(f'pinnacledb.datalayer.{database_type}.client')

    try:
        cfg = getattr(s.CFG, database_type)
    except AttributeError:
        kwargs = {}
    else:
        kwargs = cfg.dict()

    client = module.SuperDuperClient(**kwargs)
    return client.get_database_from_name(database_name)
