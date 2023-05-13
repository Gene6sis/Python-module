import datetime
from recipe import Recipe
class Book : 
    def __init__(self, name : str, recipes_list : dict, last_update : datetime = datetime.datetime.now(), creation_date : datetime = datetime.datetime.now()) :
        if not name or not isinstance(name, str) :
            raise TypeError("Name is required as string")
        if not isinstance(last_update, datetime) :
            raise TypeError("Last update as to be a datetime")
        if not isinstance(creation_date, datetime) :
            raise TypeError("Creation date as to be a datetime") 
        if not all([i in ["starter", "lunch", "dessert"] for i in recipes_list]) :
            raise TypeError("Recipes list contains unknown type")
        self.name = name
        self.recipes_list = recipes_list
        self.last_update = last_update
        self.creation_date = creation_date


    def get_recipe_by_name(self, name) -> Recipe:
        """Prints a recipe with the name \texttt{name} and returns the instance"""
        for type in self.recipes_list :
            for recipe in type :
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
        recipe_type = recipe.recipe_type
        if recipe_type in self.recipes_list :
            self.recipes_list[recipe_type].append(recipe)
        else :
            self.recipes_list[recipe_type] = [recipe]
