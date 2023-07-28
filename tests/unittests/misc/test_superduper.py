import pytest

from pinnacledb import pinnacle
from pinnacledb.misc.pinnacle import MongoDbTyper, SklearnTyper, TorchTyper


def test_mongodb_typer(test_db):
    assert MongoDbTyper.accept(test_db.db) is True


def test_sklearn_typer():
    from sklearn.linear_model import LinearRegression

    assert SklearnTyper.accept(LinearRegression()) is True


def test_torch_typer():
    import torch

    assert TorchTyper.accept(torch.nn.Linear(1, 1)) is True


def test_pinnacle_db(test_db):
    db = pinnacle(test_db.db)
    assert db.db == test_db.db


def test_pinnacle_model():
    import torch
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
