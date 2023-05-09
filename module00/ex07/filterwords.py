import sys
import string

def filterword(s : str, number : int) :
    s = [i for i in s if i not in string.punctuation]
    s = ''.join(s).split()
    print([i for i in s if len(i) > number])

if __name__ == '__main__':
    if len(sys.argv) != 3 :
        print("ERROR")
        exit(1)
    try : 
        number = int(sys.argv[2])
    except ValueError :
        print("ERROR")
        exit(1)    
    filterword(sys.argv[1], number)
