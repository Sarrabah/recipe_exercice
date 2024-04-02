import csv
def print_desirable_recipe(access_path, expected_nb_per, desired_nb_per):
    file= open(access_path)
    csvreader= csv.reader(file)
    header = next(csvreader)
    rows = []
    for row in csvreader:
        rows.append(row)
    desired_recipe={}
    for arr in rows:
        desired_recipe.update({arr[0]: (int(arr[1])/ expected_nb_per)* desired_nb_per})  
    return desired_recipe

print(print_desirable_recipe("./recipe_data.csv", 2, 4))