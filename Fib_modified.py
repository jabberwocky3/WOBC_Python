import sys
x = int(sys.argv[1])
y = int(sys.argv[2])


def Fibonacci(n):
    a, b = 1, 0
    for i in range(n):
        a, b = b, a+b
        print(a)


def Fib_modified(x, y):
    for i in range (x, y+1):
        Fibonacci(i)

if __name__ == "__main__":
    Fib_modified(x,y)
