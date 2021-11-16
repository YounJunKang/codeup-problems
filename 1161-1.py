a, b = map(int, input().split())

if a%2 == 0:
    print("짝수","+", sep="", end="")
elif a%2 == 1:
    print("홀수","+", sep="", end="")

if b%2 == 0:
    print("짝수","=", sep="", end="")
elif b%2 == 1:
    print("홀수","=", sep="", end="")

if (a+b)%2 == 0:
    print("짝수", end="")
elif (a+b)%2 != 0:
    print("홀수", end="")