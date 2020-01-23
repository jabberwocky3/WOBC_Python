#To find a list within a list

x = ['a', 'b', 'c', 'd', 'e', ['f', 'g', 'h'], 'i', 'j', 'k']

#to find g, for example:
x[5][1] #this references the 5th position in the list x, and then the 1st position in that list


#To format a print statement
x = 1.23456
#I want to only print the first two decimal spots
print("{0:.02f} is the number I want".format(x))
