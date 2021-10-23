a, b, c, n = list(map(int, input().split()))

x = a

for _ in range(n-1):
    x = x * b + c

print(x)

# x1 = a
# x2 = x1 * b + c
# x3 = x2 * b + c