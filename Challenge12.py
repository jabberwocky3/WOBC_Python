import sys, math


arg1 = int(sys.argv[1])
arg2 = int(sys.argv[2])


class Number():
    ''' Initialized with positive integer n, has 4 methods - prime, get divisors, gcd, lcm'''

    def __init__(self,x):
        self.x = x

    def is_prime(self):
        if 0 <= self.x <= 2:
            # print(f"Prime? True")
            return True


        else:
            Prime = True
            for i in range(2, self.x): #we know every number is divisible by 1 and itself, so we leave those out of the range
                if (self.x % i) == 0: #this checks if it's divisible by each value of i with a modulus of 0, which would mean it's not prime
                    # print(f"Prime? False")
                    Prime = False
                    break
        return Prime

    def get_divisors(self):
        factors = []
        i = 1
        while i <= self.x: #for all i between 1 and arg1
            if (self.x % i == 0): # determinees if the modulus of arg1/i is 0
                factors.append(i)
            i = i + 1
        return factors

    def get_gcd(self, y):
        self.y = y
        gcd = (math.gcd(self.x,y)) #built in python function to calculate gcd
        return gcd

    def get_lcm(self, y):
        self.y = y
        if self.x > y:
            greater = self.x
        else:
            greater = y

        while(True):
            if((greater % self.x == 0) and (greater % y == 0)): #iterates through values of greater, starting at the larger of x,y, to determine lcd
                lcm = greater
                break
            greater +=1
        return lcm

if __name__ == "__main__":
    number = Number(arg1) # initializes x
    print("Prime?",number.is_prime()) #off the initial value of arg1
    print("Factors:",number.get_divisors())
    print(f"GCD {arg1} and {arg2}:",number.get_gcd(arg2)) #initializes y=arg2
    print(f"LCM {arg1} and {arg2}:",number.get_lcm(arg2))
