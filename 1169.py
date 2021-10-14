age = int(input())
year = 2012 - age + 1
sex = 3 if year >= 2000 else 1
print(year % 100, sex)