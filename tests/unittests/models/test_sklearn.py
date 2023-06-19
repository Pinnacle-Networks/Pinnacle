# ruff: noqa: F401, F811

import numpy
from sklearn.svm import SVC

from pinnacledb.core.watcher import Watcher
from pinnacledb.datalayer.mongodb.query import Select
from pinnacledb.models.sklearn.wrapper import Pipeline
from tests.fixtures.collection import random_arrays, arrays, empty


def test_pipeline(random_arrays):
    X = numpy.random.randn(100, 32)
    y = (numpy.random.rand(100) > 0.5).astype(int)
    est = Pipeline('my-svc', [('my-svc', SVC())])
    est.fit(X, y)
    random_arrays.add(est)
    pl = random_arrays.models['my-svc']
    print(pl)
    random_arrays.add(
        Watcher(select=Select(collection='documents'), model='my-svc', key='x')
    )
