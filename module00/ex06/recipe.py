sandwich : dict = {
    "ingredients" : ["ham", "bread", "cheese", "tomatoes"],
    "meal" : "lunch",
    "prep_time" : 10,
}
cake : dict = {
    "ingredients" : ["flour", "sugar", "eggs"],
    "meal" : "dessert",
    "prep_time" : 60,
}
salad : dict = {
    "ingredients" : ["avocado", "arugula", "tomatoes", "spinach"],
    "meal" : "lunch",
    "prep_time" : 15,
}

cookbook : dict = {
    "Sandwich" : sandwich,
    "Cake" : cake,
    "Salad" : salad,
}

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

text : dict = {
    "Welcome" : bcolors.HEADER + "Welcome to the Python Cookbook !" + bcolors.ENDC,
    "Mode" : "List of available option:\n\t1: Add a recipe\n\t2: Delete a recipe\n\t3: Print a recipe\n\t4: Print the cookbook\n\t5: Quit\n",
    "Option" : bcolors.OKCYAN + "\033[96mPlease select an option:\n>> " + bcolors.ENDC,
    "Delete" : bcolors.WARNING + "\nPleaser enter the recipe name to delete\n> " + bcolors.ENDC,
    "Contain" : "\nHere are all the recipes :",
    "Recipe_name" : "\nPlease enter a recipe name to get its details:\n>> ",
    "Close" : "\nCookbook closed. Goodbye !",
    "Unknown" : bcolors.FAIL + "\nSorry, i don't know this recipe." + bcolors.ENDC,
    "AlreadyKnow" : bcolors.FAIL + "\nSorry, this recipe is known.\n" + bcolors.ENDC,
    "NewRecipe" : "\nEnter the name of the new recipe :\n>> ",
    "Ingredients" : "\nEnter the name of the ingredients : (Press ENTER to stop)",
    "Meal" : "\nEnter the type of meal:\n>> ",
    "Prep_time" : "\nEnter the preparation time: (minutes)\n>> ",
    "Error_number" : bcolors.FAIL + "\nA non-negative number as to be entered\n" + bcolors.ENDC,
    "Error_ingredients" : bcolors.FAIL + "\nAn ingredient as to be entered\n" + bcolors.ENDC,
    "Error_meal" : bcolors.FAIL + "\nA meal as to be entered\n" + bcolors.ENDC,
    "Error_recipe" : bcolors.FAIL + "\nA recipe as to be entered\n" + bcolors.ENDC,
}

print(text["Welcome"])
print(bcolors.OKGREEN + text["Mode"] + bcolors.ENDC)
while True : 
    mode = input(text["Option"])
    if mode == "1" : 
        #Add a recipe
        recipe = input(text["NewRecipe"]).strip().capitalize()
        if not recipe :
            print(text["Error_recipe"])
            continue
        if recipe in cookbook :
            print(text["AlreadyKnow"])
            continue
        ingredients = []
        print(text["Ingredients"])
        while True :
            newingredients = input(">> ").strip().capitalize()
            if not newingredients : break
            for new in newingredients.split() :
                if new not in ingredients : ingredients.append(new)
        if len(ingredients) == 0 :
            print(text["Error_ingredients"])
            continue
        meal = input(text["Meal"])
        if not meal :
            print(text["Error_meal"])
            continue
        try :
            prep_time = int(input(text["Prep_time"]))
        except ValueError :
            print(text["Error_number"])
            continue
        if prep_time < 0 : 
            print(text["Error_number"])
            continue
        cookbook[recipe] = {
            "ingredients" : ingredients,
            "meal" : meal,
            "prep_time" : prep_time,
        }
        print()
    elif mode == "2" :
        #Delete a recipe
        recipe = input(text["Delete"]).strip().capitalize()
        if (cookbook.pop(recipe, None) == None) :
            print(text["Unknown"])
        print()
    elif mode == "3" :	
        #Print a recipe
        recipe = input(text["Recipe_name"]).strip().capitalize()
        if recipe not in cookbook :
            print(text["Unknown"], end="\n\n")
            continue
        print(f"\nRecipe for {recipe}:")
        recipe = cookbook[recipe]
        print(f"\tIngredients list: {recipe['ingredients']}")
        print(f"\tTo be eaten for {recipe['meal']}.")
        print(f"\tTakes {recipe['prep_time']} minutes of cooking.\n")
    elif mode == "4" :
        #Print the cookbook
        print(text["Contain"])
        for recipe in cookbook :
            print(f"> {recipe}")
        print()
    elif mode == "5" :	
        print(text["Close"])
        break
    else :
        print(bcolors.FAIL + "\nSorry, this option does not exist." + bcolors.ENDC)
        print(text["Mode"])
        continue
        