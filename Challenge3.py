import sys
arg1 = int(sys.argv[1])
arg2 = int(sys.argv[2])
arg3 = str(sys.argv[3])

def Challenge3(*argv):
    ''' Takes at least 3 command line arguments, first two integers, third as string. Prints the larger of two integers; if equal it prints nothing. If the word time appears in the string, prints the sum of the integers. If both integers are odd, or one of them is a multiple of 3, it prints the string. If there are more than 3 arguments provided, prints error. '''
    if arg1 != arg2:
        print(max(arg1,arg2))

    if "time" in arg3:
        print(arg1 + arg2)

    if ((((arg1 % 2)) != 0) and ((arg2 % 2) != 0)) or ((arg1 % 3) == 0) or ((arg2 % 3) == 0):
        print(arg3)

    if len(sys.argv) > 4:
        print("error")

Challenge3(arg1, arg2, arg3)
