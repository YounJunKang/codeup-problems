n = int(input())

for x in range(1, n+1):
    for y in range(n+1-x):
        print("*", end="")
    print("")
