import sys

arg1 = str(sys.argv[1])

def non_repeat(arg1):
    ''' Takes a string from command line, and finds first non-repeating character '''

    empty = ""

    for letter in arg1: #searches in the lowercase string only
        if arg1.lower().count(letter.lower()) == 1:
            empty = letter
            break
    return empty

print(non_repeat(arg1))

if __name__ == "__main__":
    non_repeat(arg1)
