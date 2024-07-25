from typing import Iterator

import pytest
from pinnacle import pinnacle
from pinnacle.base.datalayer import Datalayer


@pytest.fixture
def db() -> Iterator[Datalayer]:
    db = pinnacle()

    yield db
    db.drop(force=True, data=True)
