a, b = map(int, input().split())

year_1 = (a//10000) + 1900
year_2 = (a//10000) + 2000

if b < 3:
    print(2012-year_1+1)
elif b > 2:
    print(2012-year_2+1)


