import pytest
from new_recipe import RecipeAdapter, RecipeReaderServiceInterface

class TestRecipeReaderService(RecipeReaderServiceInterface):
    def read_recipe_from_csv_file(self, file_path):
        formatted_file_recipe =[['Farine', '400'], ['Sucre', '50'], ['Chocolat', '200']]
        return formatted_file_recipe

def test_empty_string_path_file():
    recipe_reader = TestRecipeReaderService()
    new_recipe = RecipeAdapter(recipe_reader)
    assert new_recipe.multiply_quantity_for_n_people_from_file('', 2,5) == {}

def test_different_original_and_desired_number_of_people():
      recipe_reader = TestRecipeReaderService()
      new_recipe = RecipeAdapter(recipe_reader)
      assert new_recipe.multiply_quantity_for_n_people_from_file('./recipe_data.csv', 2, 4) == {'Farine':800.0 , 'Sucre': 100.0, 'Chocolat': 400.0} 

def test_equal_expected_and_desired_nb_per():
    recipe_reader = TestRecipeReaderService()
    new_recipe = RecipeAdapter(recipe_reader)
    assert new_recipe.multiply_quantity_for_n_people_from_file('./recipe_data.csv',2,2) == {'Farine':400.0 , 'Sucre': 50.0, 'Chocolat': 200.0} 