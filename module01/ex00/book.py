import datetime

class Book : 
    def __init__(self, name : str, last_update : datetime, creation_date : datetime, recipes_list : dict) :
        if not name or not isinstance(name, str) :
            raise TypeError("Name is required as string")
        if not isinstance(last_update, datetime) :
            raise TypeError("Last update as to be a datetime")
        if not isinstance(creation_date, datetime) :
            raise TypeError("Creation date as to be a datetime") 
        if not all([i in ["starter", "lunch", "dessert"] for i in recipes_list]) :
            raise TypeError("Recipes list contains unknown type")

