# hour, minute = input().split()

# if int(hour) != 0 and int(minute) >= 30:
#     print(hour, int(minute)-30)

# elif int(hour) != 0 and int(minute) < 30 :
#     hour = (int(hour)-1)
#     min = int(minute) + 30
#     print(hour, min)

# elif int(hour) == 0 and int(minute) < 30 :
#     min = int(minute) + 30
#     print(23, min)

# elif int(hour) == 0 and int(minute) >= 30:
#     print(hour, int(minute)-30)

hour, minute = map(int, input().split())

if hour == 0:
    hour = 24

minute = minute + hour * 60 - 30

print(minute // 60, minute % 60)