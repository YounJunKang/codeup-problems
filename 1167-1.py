a, b, c = list(map(int, input().split()))

if a >= b and b >= c:
    print(b)
elif c >= b and b >= a:
    print(b)
elif b >= a and a >= c:
    print(a)
elif c >= a and a >= b:
    print(a)
elif a >= c and c >= b:
    print(c)
elif b >= c and c >= a:
    print(c)