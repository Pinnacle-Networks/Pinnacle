import random
import warnings

import pymongo
import pytest
import pinnacle as s
from pinnacle import CFG, pinnacle
from pinnacle.base.datatype import Vector
from pinnacle.base.document import Document
from pinnacle.components.listener import Listener
from pinnacle.components.model import ObjectModel
from pinnacle.components.vector_index import VectorIndex

try:
    client = pymongo.MongoClient(CFG.data_backend)
    build_info = client.admin.command('buildInfo')

    if 'modules' in build_info and 'enterprise' in build_info['modules']:
        DO_SKIP = False
    else:
        DO_SKIP = True

    if CFG.cluster.vector_search.type != 'native':
        DO_SKIP = True

    if CFG.cluster.data_backend.type == 'native':
        DO_SKIP = False

except Exception as e:
    warnings.warn(
        f'Could not connect to MongoDB: {e} on {CFG.data_backend}; '
        'skipping Atlas tests.'
    )
    DO_SKIP = True


def random_vector_model(x):
    return [random.random() for _ in range(16)]


@pytest.fixture()
def atlas_search_config():
    previous = s.CFG.vector_search
    s.CFG.vector_search = s.CFG.data_backend
    yield
    s.CFG.vector_search = previous


@pytest.mark.skipif(DO_SKIP, reason='Only atlas deployments relevant.')
def test_setup_atlas_vector_search(atlas_search_config):
    model = ObjectModel(
        identifier='test-model',
        object=random_vector_model,
        encoder=Vector(dtype='float64', shape=(16,)),
    )
    db = pinnacle()
    collection = db['docs']

    vector_indexes = db.data_backend.list_vector_indexes()

    assert not vector_indexes

    import lorem

    db['docs'].insert([{'text': lorem.sentence()} for _ in range(50)])

    db.apply(
        VectorIndex(
            'test-vector-index',
            indexing_listener=Listener(
                model=model,
                key='text',
                select=collection.find(),
            ),
        )
    )

    assert 'test-vector-index' in db.show('vector_index')
    assert 'test-vector-index' in db.databackend.list_vector_indexes()


@pytest.mark.skipif(DO_SKIP, reason='Only atlas deployments relevant.')
def test_use_atlas_vector_search(atlas_search_config):
    db = pinnacle()

    query = (
        db['docs']
        .like(
            Document({'text': 'This is a test'}), n=5, vector_index='test-vector-index'
        )
        .select()
    )

    it = 0
    for r in db.execute(query):
        print(r)
        it += 1

    assert it == 5
