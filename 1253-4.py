a,b = map(int, input().split())

if a >= b:
    for x in range(b, a+1):
        print(x, end=" ")
elif b > a:
    for x in range(a, b+1):
        print(x, end=" ")