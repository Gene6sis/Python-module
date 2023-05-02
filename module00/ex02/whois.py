import sys

def is_integer(string) :
    if not all([i.isdigit() for i in string]) :
        print("AssertionError: argument is not an integer", file=sys.stderr)
        exit(1)
    
def definiton(string: str) :
    number: int = int(string)
    if (number == 0) : return ("Zero")
    elif (number % 2 == 1) : return ("Odd")
    return ("Even")

if len(sys.argv) > 2 : 
    print("AssertionError: more than one argument are provided", file=sys.stderr)
    exit(1)
if len(sys.argv) == 2 :
    is_integer(sys.argv[1:])
    print(f"I'm {definiton(sys.argv[1])}.")
