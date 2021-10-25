a, b = map(int, input().split())

if a >= b:
    for x in range (b, a+1):
        print(x, sep = " ")

elif a < b:
    for x in range (a, b+1):
        print(x, sep = " ")