from pinnacledb.misc.downloads import Fetcher
import os


remote = os.environ.get('SUPERDUPERDB_REMOTE_TEST', 'local')


def test_s3_and_web():
    if remote == 'remote':
        Fetcher()('s3://pinnacledb-bucket/img/black.png')
