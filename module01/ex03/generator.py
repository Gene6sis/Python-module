import random

def shuffle(List: list) -> list :
    shuffle_list = []
    while List:
        indice = random.randint(0, len(List) - 1) # Sélection aléatoire d'un indice
        mot_melange = List.pop(indice) # Retrait du mot de la liste d'origine
        shuffle_list.append(mot_melange)
    return shuffle_list

def ordered(List: list) -> list :
    List.sort()
    return List

def unique(List: list) -> list :
    List = list(dict.fromkeys(List))
    return List

def generator(text: str, sep : str = " ", option=None) :
    '''
        Splits the text according to sep value and yield the substrings.
        option precise if a action is performed to the substrings before it is yielded.
    '''
    
    if not isinstance(text, str) :
        yield "ERROR"
        return
    if not isinstance(sep, str) :
        yield "ERROR"
        return
    if option not in ["shuffle", "unique", "ordered", None] :
        yield "ERROR"
        return
    
    text = text.split(sep)
    
    if option == "shuffle" :
        text = shuffle(text)
    elif option == "unique" :
        text = unique(text)
    elif option == "ordered" :
        text = ordered(text)
    
    for word in text :
        yield word
