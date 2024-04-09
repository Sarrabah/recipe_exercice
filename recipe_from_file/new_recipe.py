from recipe import multiply_quantity_for_n_people
from recipe_reader_services import RecipeReaderService, RecipeReaderServiceInterface

class RecipeAdapter :

    def __init__(self, original_recipe_from_file : RecipeReaderServiceInterface):
        self.original_recipe_from_file = original_recipe_from_file

    def modify_the_original_recipe(self, original_recipe_from_file,original_number_of_person, desired_number_of_person):

        original_recipe = {}  
        desired_recipe= {} 
        for arr in original_recipe_from_file:
            original_recipe.update({arr[0]: int(arr[1])})  

        desired_recipe  = multiply_quantity_for_n_people(original_recipe,original_number_of_person, desired_number_of_person)
    
        return desired_recipe

    def multiply_quantity_for_n_people_from_file(self, file_path, original_number_of_person, desired_number_of_person):
        if (file_path ==''):
            return {}
        original_recipe_from_file = self.original_recipe_from_file.read_recipe_from_csv_file(file_path)
        desired_recipe = self.modify_the_original_recipe(original_recipe_from_file, original_number_of_person, desired_number_of_person)

        return desired_recipe


recipe_reader = RecipeReaderService()
new_recipe = RecipeAdapter(recipe_reader)
print(new_recipe.multiply_quantity_for_n_people_from_file('./recipe_data.csv', 2, 4))