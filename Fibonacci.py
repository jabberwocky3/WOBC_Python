import sys
n = int(sys.argv[1])


def Fibonacci(n):
    a, b = 1, 0
    for i in range(n):
        a, b = b, a+b
        print(a)



if __name__ == "__main__":
    Fibonacci(n)
