import pytest

from pinnacledb.base.exceptions import RequiredPackageNotFound
from pinnacledb.misc.annotations import requires_packages


def reqs_msg(packages):
    return f'Add following lines to requirements.txt:\n{packages}'


def test_basic_requires():
    with pytest.raises(RequiredPackageNotFound) as excinfo:
        requires_packages(['some-package'])
    assert reqs_msg('\n'.join(['some-package'])) in str(excinfo.value)


def test_versioned_requires():
    with pytest.raises(RequiredPackageNotFound) as excinfo:
        requires_packages(
            ['numpy', '10.1.0', None],
            ['requests', None, '0.1.0'],
            ['numpy', '0.0.1', '0.1.0'],
            ['requests', '0.1.0'],
            ['bad-package'],
        )
    reqs = [
        'numpy>=10.1.0',
        'requests<=0.1.0',
        'numpy>=0.0.1,<=0.1.0',
        'requests==0.1.0',
        'bad-package',
    ]
    assert reqs_msg('\n'.join(reqs)) in str(excinfo.value)
