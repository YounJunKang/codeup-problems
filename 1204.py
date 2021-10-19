# n = int(input())

# if n != 11 or n != 12 or n != 13:
#     st = n%10 
# else:
#     st = n

# if st == 1:
#     서수 = "st"
# elif st == 2:
#     서수 = "nd"
# elif st == 3:
#     서수 = "rd"
# else:
#     서수 ="th"

# print(n, 서수, sep=(""))

n = int(input())

m = n % 10
suffix = 'th'

if n not in (11, 12, 13) and m in (1, 2, 3):
    if m == 1:
        suffix = 'st'
    elif m == 2:
        suffix = 'nd'
    else:
        suffix = 'rd'

print(n, suffix, sep='')