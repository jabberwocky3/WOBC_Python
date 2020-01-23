import sys
#arg1 = str(sys.argv[1])

def counts(argv):
    ''' Function that takes a string argument and counts all of the occuring characters, then outputs the characters and the number of times they appear '''
    #input = arg1
    if len(sys.argv) > 1: #checks to see if the user provided an argument
        input = str(sys.argv[1])
        array = {} #initializes the array

        for chars in input:
                array[chars] = array.get(chars,0) + 1 #counts the number of times a character appears, and saving it to the array

        print(str(array))
    else:
        print("{}") #as per instructions, if user did not input an argument, it outputs {}


counts(input)
