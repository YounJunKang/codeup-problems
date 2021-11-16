n = int(input())

year = 2013 - n


if year >= 2000:
    print(year%100, 3)
else:
    print(year%100, 1)
