from pinnacle import Model
from pinnacle.misc.schema import get_schema


def test_get_components():

    s, a = get_schema(Model)

    assert s['validation'] == 'componenttype'
    assert s['serve'] == 'bool'
    assert s['datatype'] == 'str'
