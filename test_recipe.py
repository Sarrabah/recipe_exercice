import pytest
from recipe import print_desirable_recipe

def test_void_actual_recipe():
    assert print_desirable_recipe({}, 2,5) == {}

def test_equal_expected_and_desired_nb_per():
    assert print_desirable_recipe({"farine": 230, "sucre": 290},2,2) == {"farine": 230, "sucre": 290} 