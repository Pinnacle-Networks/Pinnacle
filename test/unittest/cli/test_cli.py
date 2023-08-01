import json

from pinnacledb.misc import run


def test_cli_info():
    data = run.out(('python', '-m', 'pinnacledb', 'info'))
    json.loads(data)
