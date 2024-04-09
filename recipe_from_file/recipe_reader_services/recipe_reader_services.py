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
