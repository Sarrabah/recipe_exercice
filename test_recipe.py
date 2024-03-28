import pytest
from recipe import print_desirable_recipe

def test_void_actual_recipe():
    assert print_desirable_recipe({}, 2,5) == {}