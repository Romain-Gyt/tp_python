from tp_recipe_scraper.Recipe import read_recipes_from_json

recipes_json = read_recipes_from_json("recipes.json")
for recipe in recipes_json:
    print(recipe)
    print("-" * 50)