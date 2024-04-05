def multiply_quantity_for_n_people(original_recipe, original_number_of_person, desired_number_of_person):
    adapted_recipe={}

    for ingredient in original_recipe.keys():
        adapted_recipe[ingredient] = (original_recipe[ingredient]/original_number_of_person)*desired_number_of_person 
    
    return adapted_recipe