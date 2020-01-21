import sys
arg1 = int(sys.argv[1])

def Challenge4(argv):
    for x in range(1, arg1 + 1):
        if x % 12 == 0:
            print(str(int(x / 12)) + " dozen")
        elif x % 3 == 0:
            print("triangle")
        elif x % 4 == 0:
            print("square")
    print(sum(range(1, arg1+1)))

Challenge4(arg1)
