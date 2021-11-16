year, month, day = list(map(int, input().split()))

fortune = (year - month + day)

if fortune%10 == 0:
    print("대박")
else:
    print("그럭저럭")