class Recipe : 
    def __init__(self, name : str, cooking_lvl : int, cooking_time : int, ingredients : list, recipe_type : str, description : str = "None"):
        if not name or not isinstance(name, str): 
            raise TypeError("Name is required")
        if cooking_lvl not in range(1, 6) or not isinstance(cooking_lvl, int):
            raise ValueError("Cooking level out of bound")
        if cooking_time < 0 or not isinstance(cooking_time, int):
            raise ValueError("Cooking time is negative")
        if not all([isinstance(i, str) for i in ingredients]) :
            raise TypeError("Ingredients must be a string")
        if recipe_type not in ["starter", "lunch", "dessert"] :
            raise ValueError("Recipe type is unknown")
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type

    def __str__(self):
        return (f'The {self.name} : \n\
        Description : {self.description} \n\
        Ingredients : {" ".join(self.ingredients)} \n\
        Cooking lvl : {self.cooking_lvl}\n\
        Cooking_time : {self.cooking_time}\n\
        Recipe type : {self.recipe_type}')

try :
    a = Recipe("42", 5, 23, ["Billy", "Bob"], "Bobby")
except (ValueError, TypeError) as error :
    print(error)
    a = None

print(a)