import string
import sys

def text_analyzer(text = None) :
    """\n\tThis function counts the number of upper characters, lower characters,\n\tpunctuation and spaces in a given text."""
    if text == None :
        text = input("What is the text to analyze?\n>> ")
    if type(text) != str :
        print("AssertionError: argument is not a string", file=sys.stderr)
        return
    dict = {'Upper' : 0, 'Lower' : 0, 'Ponctuation' : 0, 'Space' : 0}
    for letter in text :
        if letter.isupper() : dict['Upper'] += 1
        elif letter.islower() : dict['Lower'] += 1
        elif letter.isspace() : dict['Space'] += 1
        elif letter in string.punctuation : dict['Ponctuation'] += 1
    print(f"The text contains {len(text)} character(s):")
    print(f"- {dict['Upper']} upper letter(s)")
    print(f"- {dict['Lower']} lower letter(s)")
    print(f"- {dict['Ponctuation']} punctuation mark(s)")
    print(f"- {dict['Space']} space(s)")

if __name__ == '__main__':
    if (len(sys.argv) > 2) : print("Too many arguments", file=sys.stderr)
    elif (len(sys.argv) == 1) : text_analyzer(None)
    else : text_analyzer(sys.argv[1])