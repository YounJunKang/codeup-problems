a, b = map(int, input().split())

sum = 0

for x in range (a, b+1):
    if x%2 == 1:
        sum = sum + x
        if x != a:
            print("+", x, sep="", end="")
        else:
            print(x, sep="", end="")

    if x%2 == 0:
        sum = sum - x
        print("-", x, sep="", end="")


print("=", sum, sep ="")
