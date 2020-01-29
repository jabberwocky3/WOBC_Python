import sys
#arg1 = str(sys.argv[1])

def counts(argv):
    ''' Function that takes a string argument and counts all of the occuring characters, then outputs the characters and the number of times they appear '''
    #input = arg1
    if len(sys.argv) > 1:
        input = str(sys.argv[1])
        array = {}

        for chars in input:
                array[chars] = array.get(chars,0) + 1

        print(str(array))
    else:
        print("{}")

        
counts(input)
