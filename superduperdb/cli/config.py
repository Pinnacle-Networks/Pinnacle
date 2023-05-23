from . import command
import json


@command(help='Print all the SuperDuperDB configs as JSON')
def config():
    # This won't work until the configs commit is pulled
    from pinnacledb import CFG

    print(json.dumps(CFG.dict(), indent=2))
