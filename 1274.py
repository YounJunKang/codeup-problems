n = int(input())

isPrime = True
for x in range(2, n):
    if n % x == 0:
        isPrime = False
        break

if isPrime:
    print('prime')
else:
    print('not prime')