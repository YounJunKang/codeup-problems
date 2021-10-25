n = int(input())

digit = 0
while n > 0:
    digit += 1
    n = n // 10

print(digit)