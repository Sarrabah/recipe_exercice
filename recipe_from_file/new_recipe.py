from recipe import multiply_quantity_for_n_people
from abc import ABC, abstractmethod

class RecipeReaderServiceInterface(ABC):
    @abstractmethod
    def read_recipe_from_csv_file(self, file_path):
        ...

class RecipeReaderService(RecipeReaderServiceInterface):

    def read_recipe_from_csv_file(self, file_path):

        file= open(file_path)
        content = file.readlines()
        rows = content[1:]

        recipe=[]
        for row in range(len(rows)):
            element = rows[row].strip().split(",")
            recipe.append(element)
        file.close()

        return recipe 


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
   
        original_recipe_from_file = self.original_recipe_from_file.read_recipe_from_csv_file(file_path)
        desired_recipe = self.modify_the_original_recipe(original_recipe_from_file, original_number_of_person, desired_number_of_person)

        return desired_recipe


recipe_reader = RecipeReaderService()
new_recipe = RecipeAdapter(recipe_reader)
print(new_recipe.multiply_quantity_for_n_people_from_file('./recipe_data.csv', 2, 4))