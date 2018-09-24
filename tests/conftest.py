import functools
import os

import pytest
import uuid


def remove_file_if_exists(path):
    if os.path.exists(path):
        os.remove(path)


@pytest.fixture()
def test_file(request):
    file_path = '/tmp/{}'.format(uuid.uuid4().hex)
    with open(file_path, 'w') as f:
        f.write('temp')
    request.addfinalizer(functools.partial(remove_file_if_exists, file_path))
    return file_path
