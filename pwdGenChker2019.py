import sys, string, re
arg1 = sys.argv[1]

def password_check(testString):
    '''Checks to see if input string meets the following conditions#'''
    '''Length >= 14; Includes one or more each of Uppercase, Lowercase, Numbers, Specials'''
    '''Not more than 3 consecutive characters from same set'''
    '''No whitespace; Returns True if valid, False if invalid password'''

    #establish a variable test to contain whether or not each test is valid or invalid
    test = True

    #check for length >= 14#
    if not len(testString) >= 14:
        test = False

    #Make sure the string contains at least one each of the character sets
    #Test for upper
    if not any(char in string.ascii_uppercase for char in testString):
        test = False
    #Test for lowercase
    if not any(char in string.ascii_lowercase for char in testString):
        test = False
    #Test for Numbers
    if not any(char in string.digits for char in testString):
        test = False
    #Test for special characters
    if not any(char in string.punctuation for char in testString):
        test = False

    #Test to find any instances of 4 or more characters, in a row, from the above sets
    #Tried using FOR loops... too complicated. Google showed the REGEX way, so importing
    #the module re and using the regex versions of the string.ascii_lowercase(etc)
    #works faster than the for loop
    Row4Upper = re.findall("[A-Z]{4}[A-Z]*", testString)
    if len(Row4Upper) > 0:
        test = False

    Row4Lower = re.findall("[a-z]{4}[a-z]*", testString)
    if len(Row4Lower) > 0:
        test = False

    Row4Number = re.findall("[0-9]{4}[0-9]*", testString)
    if len(Row4Number) > 0:
        test = False

    Row4Special = re.findall("[^a-zA-Z0-9]{4}[^a-zA-Z0-9]*", testString)
    if len(Row4Special) > 0:
        test = False


    #Test to make sure there's no white space
    if any(char in string.whitespace for char in testString):
        test = False


    if test == True:
        return True
    else:
        return False

def password_checker(tested):
    testString = tested
    if password_check(testString) == True:
        return True
    else:
        return False

# if __name__ == "__main__":
#     password_checker(arg1)
password_checker(arg1)
