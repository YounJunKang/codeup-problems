a, b = map(int, input().split())

sum = 0

for x in range (a, b+1):
    if x % 2 == 0:
        sum = sum - x
        print("-",x, end ="", sep ="")

    if x % 2 == 1:
        sum = sum + x
        print("+",x, end ="", sep="")

print("=", sum, sep = "")