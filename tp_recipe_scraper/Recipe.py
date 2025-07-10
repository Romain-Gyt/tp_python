# recipe_reader.py
import json


class Recipe:
    def __init__(self, number, url, title, ingredients, instructions, nutrients):
        self.number = number
        self.url = url
        self.title = title
        self.ingredients = ingredients
        self.instructions = instructions
        self.nutrients = nutrients

    def __str__(self):
        return (f"Recette {self.number}: {self.title}\n"
                f"URL: {self.url}\n"
                f"Ingrédients: {', '.join(self.ingredients)}\n"
                f"Instructions: {self.instructions}\n"
                f"Nutriments: {self.nutrients}\n")


def read_recipes_from_json(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)

    recipes = []
    for item in data:
        recipe = Recipe(
            number=item.get("number"),
            url=item.get("url"),
            title=item.get("title"),
            ingredients=item.get("ingredients", []),
            instructions=item.get("instructions", ""),
            nutrients=item.get("nutrients", {})
        )
        recipes.append(recipe)

    return recipes
