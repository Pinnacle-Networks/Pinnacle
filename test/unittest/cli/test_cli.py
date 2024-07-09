import json

from pinnacle.misc import run


def test_cli_info():
    data = run.out(('python', '-m', 'pinnacle', 'info')).strip()
    assert data.startswith('```') and data.endswith('```')
    json.loads(data[3:-3])
