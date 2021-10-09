a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
d = (b if a>b else b) if ((b if a>b else b)<c) else c
print(d)