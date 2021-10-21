a, b = map(int,input().split())

if a>=b:
    for c in range (b, a+1):
        print(c, end=" ")

if b>a:
    for c in range (a, b+1):
        print(c, end=" ")