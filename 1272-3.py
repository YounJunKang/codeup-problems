a, b = map(int, input().split())

# n = 1, 10, 2, 20, 3, 30,

import math

if a%2 ==1:
    a = math.ceil(a/2)
 

elif a%2 ==0:
    a = (a//2)*10 

if b%2 ==1:
    b = math.ceil(b/2)
    

elif b%2 ==0:
    b = (b//2)*10

print(a+b)