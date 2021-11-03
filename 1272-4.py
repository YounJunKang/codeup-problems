a, b = map(int, input().split())

odd = 0
even = 0

if a % 2 == 0:
    even = (even + a)*5
elif a % 2 == 1:
    odd = odd + a

if b % 2 == 0:
    even = (even + b)*5
elif b % 2 == 1:
    odd = odd +b

print(odd+even)