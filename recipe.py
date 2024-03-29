def print_desirable_recipe(actual_recipe, expected_nb_per, desired_nb_per):
    if actual_recipe == {} or expected_nb_per == desired_nb_per :
        return actual_recipe
    else:
        final_recipe={}
        for key in actual_recipe.keys():
            final_recipe[key] = (actual_recipe[key]/expected_nb_per)*desired_nb_per 
        return final_recipe