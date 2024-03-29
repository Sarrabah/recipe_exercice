def print_desirable_recipe(actual_recipe, expected_nb_per, desired_nb_per):
    if actual_recipe == {}:
        return actual_recipe
    elif expected_nb_per == desired_nb_per:
        return actual_recipe