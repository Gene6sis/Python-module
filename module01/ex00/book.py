import datetime
from recipe import Recipe
class Book : 
    def __init__(self, name : str) :
        if not name or not isinstance(name, str) :
            raise TypeError("Name is required as string")
        self.name = name
        self.recipes_list = {
            'starter': [],
            'lunch': [],
            'dessert': []
        }
        self.creation_date = datetime.datetime.now()
        self.last_update = self.creation_date


    def get_recipe_by_name(self, name) -> Recipe:
        """Prints a recipe with the name \texttt{name} and returns the instance"""
        for type in self.recipes_list :
            for recipe in self.recipes_list[type] :
                if recipe.name == name :
                    print(str(recipe))
                    return recipe
        return None

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        if recipe_type in self.recipes_list :
            return self.recipes_list[recipe_type]
        return None
        
    def add_recipe(self, recipe : Recipe):
        """Add a recipe to the book and update last_update"""
        if not isinstance(recipe, Recipe) : 
            return
        self.recipes_list[recipe.recipe_type].append(recipe)
        self.last_update = datetime.datetime.now()
