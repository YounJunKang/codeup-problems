birthday, gender = input().split()

birthday = int(birthday)
gender = int(gender)

age = birthday//10000

if (gender == 1) or (gender == 2):
    print(2012 - (1900+age)+1)

elif (gender == 3) or (gender == 4):
    print(2012 -(2000+age)+1)