import pandas as pd

from pinnacledb.misc.text import contextualize


def test_simple_contextualize():
    df = pd.DataFrame({'text': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']})
    context = contextualize(df, 3, 1)
    assert len(context) == 7
