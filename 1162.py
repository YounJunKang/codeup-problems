a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)


#1902 3 15
#1902 2 10 -> 1910

if (a-b+c)%10 == 0:
    print("대박")
else:
    print("그럭저럭")