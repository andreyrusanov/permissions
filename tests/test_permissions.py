import os
import pytest

from permissions import get_permissions_from


@pytest.mark.parametrize('permission_to_set,expected', ((055, False), (455, True)))
def test_readable_check(test_file, permission_to_set, expected):
    os.chmod(test_file, permission_to_set)
    assert get_permissions_from(test_file).readable is expected


@pytest.mark.parametrize('permission_to_set,expected', ((455, False), (755, True)))
def test_executable_check(test_file, permission_to_set, expected):
    os.chmod(test_file, permission_to_set)
    assert get_permissions_from(test_file).executable is expected


@pytest.mark.parametrize('permission_to_set,expected', ((655, False), (755, True)))
def test_writable_check(test_file, permission_to_set, expected):
    os.chmod(test_file, permission_to_set)
    assert get_permissions_from(test_file).executable is expected


# @pytest.mark.parametrize('permission_to_set,expected', (
#         (600, '0600'),
#         (755, '0755')
# ))
# def test_chmod(test_file, permission_to_set, expected):
#     pass
# #
# #
# # def test_umask(test_file):
# #     pass
