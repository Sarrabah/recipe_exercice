import pytest
from recipe import print_desirable_recipe

def test_void_actual_recipe():
    assert print_desirable_recipe({}, 2,5) == {}

def test_equal_expected_and_desired_nb_per():
    assert print_desirable_recipe({"farine": 230, "sucre": 290},2,2) == {"farine": 230, "sucre": 290} 

def test_different_expected_and_desired_nb_per() :
    assert print_desirable_recipe({"farine": 200, "sucre": 100},2,4) == {"farine": 400, "sucre": 200}

def test_desired_nb_per_equal_to_zero() :
    assert print_desirable_recipe({"farine": 200, "sucre": 100},2,0) == {"farine": 0, "sucre": 0}