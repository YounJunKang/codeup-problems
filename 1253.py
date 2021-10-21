a, b = map(int, input().split())

if a >= b: 
    for a in range(b, a+1):
        print(a, end=" ")
    
if b > a:
    for b in range(a, b+1):
        print(b, end=" ")