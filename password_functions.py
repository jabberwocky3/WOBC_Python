import random, sys, string

#Allow for optional input for arg1. If provided, ensure it's greater than or equal to 14
# if len(sys.argv) > 1:
#     arg1 = sys.argv[1]
#     arg1 = int(arg1)
# else:
#     arg1 = 14
#
# if arg1 < 14:
#     arg1 = 14



# def joiner(x):
# 	return (''.join(x))

def password_generator(arg1=14):
	#Sets the default length as 14'''
    #Generates a password that ensures the following conditions are met:'''
    #Length >= 14; Includes one or more each of Uppercase, Lowercase, Numbers, Specials'''
    #Not more than 3 consecutive characters from same set; No whitespace'''

		password = []
		i = 0
		arg1 = int(arg1)
		while i < (arg1):
			password.extend(random.choice(string.ascii_lowercase))
			i += 1
			if i == (arg1):
				break
			password.append(random.choice(string.ascii_uppercase))
			i += 1
			if i == (arg1):
				break
			password.append(random.choice(string.punctuation))
			i += 1
			if i == (arg1):
				break
			password.append(random.choice(string.digits))
			i += 1
		final = ''.join(password)
		return (final)
