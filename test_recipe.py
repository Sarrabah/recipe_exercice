import pytest
from recipe import multiply_quantity_for_n_people

def test_void_actual_recipe():
    assert multiply_quantity_for_n_people({}, 2,5) == {}

def test_equal_expected_and_desired_nb_per():
    assert multiply_quantity_for_n_people({"farine": 230, "sucre": 290},2,2) == {"farine": 230, "sucre": 290} 

def test_different_expected_and_desired_nb_per() :
    assert multiply_quantity_for_n_people({"farine": 200, "sucre": 100},2,4) == {"farine": 400, "sucre": 200}

def test_desired_nb_per_equal_to_zero() :
    assert multiply_quantity_for_n_people({"farine": 200, "sucre": 100},2,0) == {"farine": 0, "sucre": 0}

def test_actual_recipe_zero_quantities() :
    assert multiply_quantity_for_n_people({"farine": 0, "sucre": 0},2,12) == {"farine": 0, "sucre": 0}