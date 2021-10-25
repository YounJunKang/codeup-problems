a, b = map(int, input().split())

s = 0

for x in range (a, b+1):
    if x%3 == 0:
        s = s+x
        
print(s)