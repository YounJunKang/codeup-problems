a = int(input())
b = int(input())

rate = list(map(int, input().split()))

total = a

for x in rate:
    x = (x+100)*0.01
    a = a*x 

new_total = a

import math

interest = new_total - total
interest = round(interest)
print(interest)

if interest > 0:
    print("good")
elif interest == 0:
    print("same")
elif interest < 0:
    print("bad")

