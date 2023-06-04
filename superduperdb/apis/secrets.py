import importlib
from pinnacledb import CFG


def client_init():
    for provider in CFG.apis.providers:
        importlib.import_module(f'pinnacledb.apis.{provider}.init').init_fn()
