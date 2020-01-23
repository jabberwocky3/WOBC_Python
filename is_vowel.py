import sys
arg1 = sys.argv[1]
vowel = ['a','e','i','o','u','A', 'E', 'I', 'O', 'U']

def is_vowel(n):
    if arg1 in vowel:
        print(f"{arg1} is a vowel")
    else:
        print(f"{arg1} is not a vowel")


if __name__ == "__main__":
    is_vowel(arg1)
