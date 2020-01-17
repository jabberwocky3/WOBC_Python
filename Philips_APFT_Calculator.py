import AgeRange

def main()
    age = int(input('Input your age:'))
    gender = input('Input your gender (M/F): ')
    pushups = int(input('Input the number of pushups: '))
    situps = int(input('Input the number of situps: '))
    runMin = int(input('Input the number of run minutes: '))
    runSec = int(input('Input the number of run seconds: '))
    runTime = ((runMin * 60) + runSec)

AgeRange(age)
AgeGroup = AgeRange(age)
print (f"Your age group is: ", AgeGroup)
