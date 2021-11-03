n = int(input())

#a*b = n
c = []

for x in range (1, n):
    if n % x == 0:
        c.append(x)

d = []

for x2 in(2, c):
    if n%x2 == 0:
        d.append(x2)

print(d)

