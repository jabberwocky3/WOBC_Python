import sys
arg1 = int(sys.argv[1])
fib=[0,1]

def fibonacci(arg1):
    if arg1 == 0:
        return fib[0]
    elif arg1 == 1:
        return fib
    else:
        for i in range(2,arg1):
            fib.append(fib[i-2] + fib[i-1])
    return fib

def which_fibonacci(arg1):
    ''' Receives a non-negative integer, checks to see if it's a Fibonacci number and returns its position. If the argument is not a Fibonacci number, it returns 0'''
    fib = [0,1] #baselines the fib list

    while (fib[-1] < arg1): #checks to see if the last value is less than arg1
        fib.append(fib[-1] + fib[-2]) #adds the next fibonacci number

    if arg1 in fib: #checks to see if arg1 is in our list, hence a fibonacci number
        print(f"Index:",fib.index(arg1)+1) #the +1 accounts for the 0 index as 1st position
    else: #if arg1 is not a fibonacci number, it returns 0
        print("Index: 0")


def next_fibonacci(arg1):
    ''' Receives a non-negative integer and returns the next largest Fibonacci number '''
    fib=[0,1] #re-establishes the list to 0,1; not necessary if executing which_fibonacci and next_fibonacci separately
    # fibonacci(2) #baselines

    while (fib[-1] <= arg1): #by saying <=, it will iterate one more time if we pass a fibonacci number, hence leaving us with the NEXT value as the last value
        fib.append(fib[-1] + fib[-2])
    print(f"Next: ",fib[-1])


if __name__ == "__main__":
    which_fibonacci(arg1)
    next_fibonacci(arg1)
