a, b = map(int, input().split())

# if a%2 == 0:
#     for c in range (a+1, b+1, 2):
#         print(c, end=" ")

# if a%2 == 1:
#     for c in range (a, b+1, 2):
#         print(c, end=" ")

for x in range(a, b+1):
    if x % 2 == 1:
        print(x, end=' ')

# print(*[x for x in range(a, b+1) if x % 2 == 1])