year, classroom, number = input().split()


if int(classroom) < 10:
    classroom = '0' + classroom

if int(number) < 10:
    number = '00' + number
elif int(number) < 100:
    number = '0' + number

print(year, classroom, number, sep="")
