from recipe import *
from book import *

# Testing error recipe :

# Name empty
try :
    test = Recipe("", 1, 1, ["Legumes", "Love"], "starter", "Hello World!")
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



# Good Recipe :

Ratatouille = Recipe("Ratatouille", 1, 45, ["Legumes", "Love"], "lunch", "Si on peut plus faire profiter les copains")
Tiramisu = Recipe("Tiramisu", 5, 60, ["Boudoir", "Chocolat", "Speculos"], "dessert", "Le meilleur de tous <3")
Cake = Recipe("Cake", 4, 40, ["Stawberry", "Sugar"], "dessert")
Quiche = Recipe("Quiche", 3, 500, ["A lot of everything", "Potato"], "lunch")
Salade = Recipe("Salade", 1, 10, ["Salad", "Tomato", "Sauce"], "starter")
Pain = Recipe("Bread", 2, 20, ["Flour", "Love"], "starter", "Le pain de chez nous")


dico = {
}


# Book Error :
# Name empty
try : 
    test = Book("", {})
except (ValueError, TypeError) as error :
    test = None
    print(f"Error : {error}\nValue : {test}")
# Name is not a string
# Last update is not a datetime
# Creation date is not a datetime
# 



