a, b = map(int, input().split())

s = 0

for x in range (a, b+1):
    if x != a:
        if x%2 != 0:
            print("+",x, sep="", end="")
        elif x%2 ==0:
            print("-",x, sep="", end="")
    elif x == a:
        if x%2 == 0:
            print("-", x, sep="", end="")
        elif x%2 != 0:
            print(x, end="")

for x in range(a, b+1):
    if x%2 != 0:
        s = s+x
    elif x%2 ==0:
        s = s-x
print("=", s, sep="", end="")