import os
import tempfile
import uuid

import pytest

from pinnacledb import CFG
from pinnacledb.backends.mongodb.query import Collection
from pinnacledb.base.document import Document
from pinnacledb.ext.pillow.encoder import pil_image
from pinnacledb.misc.download import Fetcher

remote = os.environ.get('SDDB_REMOTE_TEST', 'local')


def test_s3_and_web():
    if remote == 'remote':
        Fetcher()('s3://pinnacledb-bucket/img/black.png')


@pytest.fixture
def patch_cfg_downloads(monkeypatch):
    monkeypatch.setattr(CFG.downloads, 'hybrid', True)
    td = str(uuid.uuid4())
    with tempfile.TemporaryDirectory() as td:
        monkeypatch.setattr(CFG.downloads, 'root', td)
        yield


def test_file_blobs(local_empty_db, patch_cfg_downloads, image_url):
    to_insert = [
        Document(
            {
                'item': {
                    '_content': {
                        'uri': image_url,
                        'encoder': 'pil_image',
                    }
                },
                'other': {
                    'item': {
                        '_content': {
                            'uri': image_url,
                            'encoder': 'pil_image',
                        }
                    }
                },
            }
        )
        for _ in range(2)
    ]

    local_empty_db.execute(
        Collection('documents').insert_many(to_insert), encoders=(pil_image,)
    )
    local_empty_db.execute(Collection('documents').find_one())
    assert os.listdir(CFG.downloads.root)
