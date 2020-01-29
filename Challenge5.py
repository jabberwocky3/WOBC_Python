import sys
arg1 = int(sys.argv[1])


def factorial(argv):
    factorial = 1
    if arg1 < 0:
        print("Please enter a positive integer")
    elif arg1 == 0:
        print("1")
    else:
        for i in range(1,arg1 + 1):
            factorial = factorial * i
        print(factorial)

factorial(arg1)
