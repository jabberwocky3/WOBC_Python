import random, string

#Must have a function called from another function, so we use the join
def final(password):
    return (''.join(password))

def password_generator(arg1=14):
    '''Sets the default length as 14
    Generates a password that ensures the following conditions are met:
    Length >= 14; Includes one or more each of Uppercase, Lowercase, Numbers, Specials
    Not more than 3 consecutive characters from same set; No whitespace'''

    password = [] #builds our empty password field
    length = 0 #starts at length 0 to iterate

    arg1 = int(arg1) #ensures we have an integer from the argument

    if arg1 < 14: #makes sure we generate 14 if the user inputs less
        arg1 = 14

    while length < (arg1): #will iterate until the length field is equal to the length specified by arg1
        password.append(random.choice(string.ascii_lowercase))
        length += 1
        if length == (arg1):
            break
        password.append(random.choice(string.ascii_uppercase))
        length += 1
        if length == (arg1):
            break
        password.append(random.choice(string.punctuation))
        length += 1
        if length == (arg1):
            break
        password.append(random.choice(string.digits))
        length += 1

    #Here's where we call the other function to meet the assignment instructions
    finalPassword = final(password)
    return (finalPassword)
