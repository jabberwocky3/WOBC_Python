import sys
arg1 = int(sys.argv[1])

def Challenge4(argv):
    ''' Takes one command line integer argument. For each number between 1 and the argument that is a multiple of three, it prints the word triangle. For each number in the range that is a multiple of 4, it prints square. If it is a multiple of 12, it neither prints square or triangle, but it prints X Dozen where X is the the number of dozens you're at. Finally, prints the sum of numbers between 1 and the argument, inclusively.'''
    for x in range(1, arg1 + 1):
        if x % 12 == 0:
            print(str(int(x / 12)) + " dozen")
        elif x % 3 == 0:
            print("triangle")
        elif x % 4 == 0:
            print("square")
    print(sum(range(1, arg1+1)))

Challenge4(arg1)
