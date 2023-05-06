import sys

def operations(a : int, b : int) : 
    print(f"Sum:        {a+b}")
    print(f"Difference: {a-b}")
    print(f"Product:    {a*b}")
    print(f"Quotient:   {a/b if (b != 0) else 'ERROR (division by zero)'}")
    print(f"Remainder:  {a%b if (b != 0) else 'ERROR (modulo by zero)'}")

if __name__ == '__main__':
    if (len(sys.argv) < 3) : print("Usage: python operations.py <number1> <number2>\nExample\n\tpython operations.py 10 3")
    elif (len(sys.argv) > 3) : print("AssertionError: too many arguments", file=sys.stderr)
    elif (not all([i.isdigit() for i in sys.argv[1:]])) : print("AssertionError: only integers")
    else : operations(int(sys.argv[1]), int(sys.argv[2]))