import sys

morse = { 'A':'.-', 'B':'-...',
	'C':'-.-.', 'D':'-..', 'E':'.',
	'F':'..-.', 'G':'--.', 'H':'....',
	'I':'..', 'J':'.---', 'K':'-.-',
	'L':'.-..', 'M':'--', 'N':'-.',
	'O':'---', 'P':'.--.', 'Q':'--.-',
	'R':'.-.', 'S':'...', 'T':'-',
	'U':'..-', 'V':'...-', 'W':'.--',
	'X':'-..-', 'Y':'-.--', 'Z':'--..',
	'1':'.----', '2':'..---', '3':'...--',
	'4':'....-', '5':'.....', '6':'-....',
	'7':'--...', '8':'---..', '9':'----.',
	'0':'-----', ' ': '/'
}

def decrypt(message: str) :
    print(*[morse[letter] for letter in message], sep=' ')

if __name__ == '__main__':
    if len(sys.argv) > 1 :
        message = ' '.join(sys.argv[1:]).upper()
        if not all([i.isalpha() or i.isnumeric() or i==' ' for i in message]) :
            print("Error")
        else :
            decrypt(message)