n = int(input())

#1, n-2, n
#1, n-4, n-2, n 
#1, n-6, n-4, n-2, n
s = 0

for x in range(1, n+1):
    if x%2 == 1:
        for y in range(x):
            if y > n:
                for z in range(1, (n-y)/2):
                    print(" ", end="")
                print("")
                for g in range(1, y):
                    print("*", end="")
                print("")
            else:
                for d in range(1, y):
                    print("*", end="")