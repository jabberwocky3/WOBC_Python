import sys
arg1 = int(sys.argv[1])
fib = []

def fibonacci(n):
    a, b = 1, 0
    for i in range(n):
        a, b = b, a+b
        fib.append(a)

# def fib2(n):
#     if len(fib) >= n:
#         return fib[n-1]

def which_fibonacci(arg1):
    ''' Receives a non-negative integer, checks to see if it's a Fibonacci number and returns its position. If the argument is not a Fibonacci number, it returns 0'''

    fibonacci(0)

    while (fib.index(-1) < arg1):
        fibonacci(arg1+1) #needs a statement to handle if the last value of fib is LESS than arg1
        if (fib[-1] > arg1):
            break
    if arg1 in fib:
        print((fib.index(arg1))+1)
    else:
        print("0")


# def next_fibonacci():
#     ''' Receives a non-negative integer and returns the next largest Fibonacci number '''
#     fibonacci(arg1)
#     while arg1 in lib = False:
#         arg1 +=1
#     print(fib.index(arg1))


#
#
# which_fibonacci(arg1)
which_fibonacci(arg1)
