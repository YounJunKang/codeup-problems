year, month, day = list(map(int, input().split()))

fortune = year+month+day

if (fortune//100)%2 == 0:
    print("대박")

if (fortune//100)%2 == 1:
    print("그럭저럭")