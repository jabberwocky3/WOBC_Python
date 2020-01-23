# import sys
# arg1 = int(sys.argv[1])
# arg2 = int(sys.argv[2])

class Number():
    ''' Initialized with positive integer n, has 4 methods - prime, get divisors, gcd, lcm'''

    def __init__(self,n):
        self.n = n

    def is_prime(self):
        for i in range(2, self.n): #we know every number is divisible by 1 and itself, so we leave those out of the range
            if (self.n % i) == 0: #this checks if it's divisible by each value of i with a modulus of 0, which would mean it's not prime
                return False
                break
            else:
                return True # if all values of i do not produce the modulus == 0, the number is prime

    def get_divisors(self):
        i = 1
        while i <= self.n:
            if (n % i ==0):
                print(i)
            i = i + 1

    def get_gcd(self, x):
        self.x = arg1
        pass

    def get_lcm(self, x):
        blah blah
        pass
