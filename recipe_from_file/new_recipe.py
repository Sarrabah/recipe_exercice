from recipe import multiply_quantity_for_n_people

def read_recipe_from_csv_file(file_path):

    file= open(file_path)
    content = file.readlines()
    rows = content[1:]

    recipe=[]
    for row in range(len(rows)):
        element = rows[row].strip().split(",")
        recipe.append(element)
    file.close()

    return recipe 

def modify_the_original_recipe(original_recipe_from_file,original_number_of_person, desired_number_of_person):

    original_recipe= {}  
    desired_recipe= {} 
    for arr in original_recipe_from_file:
        original_recipe.update({arr[0]: int(arr[1])})  
    
    desired_recipe  = multiply_quantity_for_n_people(original_recipe,original_number_of_person, desired_number_of_person )
    
    return desired_recipe

def multiply_quantity_for_n_people_from_file(file_path, original_number_of_person, desired_number_of_person):
   
    original_recipe_from_file = read_recipe_from_csv_file(file_path)
    desired_recipe = modify_the_original_recipe(original_recipe_from_file,original_number_of_person, desired_number_of_person)
    return desired_recipe


if __name__ == "__main__" :
    print(multiply_quantity_for_n_people_from_file("./recipe_data.csv", 2, 4))