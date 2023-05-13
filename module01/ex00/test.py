from recipe import *
from book import *

# Testing error recipe :

# Name empty && not a string
try :
    test = Recipe("", 1, 1, ["Legumes", "Love"], "starter", "Hello World!")
except (ValueError, TypeError) as error :
    test = None
    print(f"Error : {error}\nValue : {test}")

try :
    test = Recipe(42, 1, 1, ["Legumes", "Love"], "starter", "Hello World!")
except (ValueError, TypeError) as error :
    test = None
    print(f"Error : {error}\nValue : {test}")

# Cooking lvl out of range
try :
    test = Recipe("Test_plat", 0, 1, ["Legumes", "Love"], "starter", "Hello World!")
except (ValueError, TypeError) as error :
    test = None
    print(f"Error : {error}\nValue : {test}")

try :
    test = Recipe("Test_plat", 6, 1, ["Legumes", "Love"], "starter", "Hello World!")
except (ValueError, TypeError) as error :
    test = None
    print(f"Error : {error}\nValue : {test}")

# Cooking time negative
try :
    test = Recipe("Test_plat", 1, -42, ["Legumes", "Love"], "starter", "Hello World!")
except (ValueError, TypeError) as error :
    test = None
    print(f"Error : {error}\nValue : {test}")

# Ingredients other type
try :
    test = Recipe("Test_plat", 1, 1, [42, "Love"], "starter", "Hello World!")
except (ValueError, TypeError) as error :
    test = None
    print(f"Error : {error}\nValue : {test}")

# Ingredients empty
try :
    test = Recipe("Test_plat", 1, 1, ["", "", ""], "starter", "Hello World!")
except (ValueError, TypeError) as error :
    test = None
    print(f"Error : {error}\nValue : {test}")

# Recipe_type empty
try :
    test = Recipe("Test_plat", 1, 1, ["Legumes", "Love"], "", "Hello World!")
except (ValueError, TypeError) as error :
    test = None
    print(f"Error : {error}\nValue : {test}")

# Recipe_type unknown
try :
    test = Recipe("Test_plat", 1, 1, ["Legumes", "Love"], "bob", "Hello World!")
except (ValueError, TypeError) as error :
    test = None
    print(f"Error : {error}\nValue : {test}")




# Book Error :
# Name empty
try : 
    test = Book("")
except (ValueError, TypeError) as error :
    test = None
    print(f"Error : {error}\nValue : {test}")

# Name is not a string
try : 
    test = Book(42)
except (ValueError, TypeError) as error :
    test = None
    print(f"Error : {error}\nValue : {test}")




# Good Recipe :

Ratatouille = Recipe("Ratatouille", 1, 45, ["Legumes", "Love"], "lunch", "Si on peut plus faire profiter les copains")
Quiche = Recipe("Quiche", 3, 500, ["A lot of everything", "Potato"], "lunch")
Tiramisu = Recipe("Tiramisu", 5, 60, ["Boudoir", "Chocolat", "Speculos"], "dessert", "Le meilleur de tous <3")
Cake = Recipe("Cake", 4, 40, ["Stawberry", "Sugar"], "dessert")
Salade = Recipe("Salade", 1, 10, ["Salad", "Tomato", "Sauce"], "starter")
Pain = Recipe("Bread", 2, 20, ["Flour", "Love"], "starter", "Le pain de chez nous")

print();print();print();print();print();print()

# Test 
book = Book("Marmiton")
print("Empty")
print(book.get_recipes_by_types("starter"))
print(book.get_recipes_by_types("lunch"))
print(book.get_recipes_by_types("dessert"))
print("Add ratatouille")
book.add_recipe(Ratatouille)
print(*book.get_recipes_by_types("lunch"), sep='\n', end='\n\n')
print("Add Quiche")
book.add_recipe(Quiche)
print(*book.get_recipes_by_types("lunch"), sep='\n', end='\n\n')

print("Empty")
print(book.get_recipes_by_types("starter"))
print(book.get_recipes_by_types("dessert"))

print("Add Tiramisu, Cake, Salade, Pain")
book.add_recipe(Tiramisu)
book.add_recipe(Cake)
book.add_recipe(Salade)
book.add_recipe(Pain)

print("Starter : ")
print(*book.get_recipes_by_types("starter"), sep='\n', end='\n\n')
print("Lunch : ")
print(*book.get_recipes_by_types("lunch"), sep='\n', end='\n\n')
print("Dessert : ")
print(*book.get_recipes_by_types("dessert"), sep='\n', end='\n\n')

print("Search Bread")
a = book.get_recipe_by_name("Bread")
print(a)

