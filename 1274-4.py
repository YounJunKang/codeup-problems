num = int(input())

is_prime = True

for x in range(2, num):
    if num % x == 0:
        is_prime = False
        break

if is_prime:
    print("prime")
else:
    print("not prime")

