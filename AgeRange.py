age = int(input('Input your age in years: '))


def AgeRange(age):
    if ((age >=17) and (age < 22)):
        AgeGroup == '17-21'
    elif ((age >= 22) and (age < 27)):
        AgeGroup == '22-26'
    elif ((age >= 27) and (age < 32)):
        AgeGroup == '27-32'
    elif ((age >= 32) and (age < 37)):
        AgeGroup == '32-36'
    elif ((age >= 37) and (age < 42)):
        AgeGroup == '37-41'
    elif ((age >= 42) and (age < 47)):
        AgeGroup == '42-46'
    elif ((age >= 47) and (age < 52)):
        AgeGroup == '47-52'
    elif ((age >= 52) and (age < 57)):
        AgeGroup == '52-56'
    elif ((age >= 57) and (age < 62)):
        AgeGroup == '57-61'
    elif (age >= 62):
        AgeGroup == '62+'
    return AgeGroup

AgeGroup = AgeRange(age)
