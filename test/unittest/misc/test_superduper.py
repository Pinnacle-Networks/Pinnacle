import pytest

try:
    import torch
except ImportError:
    torch = None

from pinnacledb import pinnacle
from pinnacledb.misc.pinnacle import SklearnTyper, TorchTyper


def test_sklearn_typer():
    from sklearn.linear_model import LinearRegression

    assert SklearnTyper.accept(LinearRegression()) is True


@pytest.mark.skipif(not torch, reason='Torch not installed')
def test_torch_typer():
    assert TorchTyper.accept(torch.nn.Linear(1, 1)) is True


@pytest.mark.skipif(not torch, reason='Torch not installed')
def test_pinnacle_model():
    from sklearn.linear_model import LinearRegression

    model = pinnacle(torch.nn.Linear(1, 1))
    assert isinstance(model.object.artifact, torch.nn.modules.linear.Linear)
    model = pinnacle(LinearRegression())
    assert isinstance(model.object.artifact, LinearRegression)


def test_pinnacle_raise():
    with pytest.raises(NotImplementedError):
        pinnacle(1)

    with pytest.raises(NotImplementedError):
        pinnacle("string")
