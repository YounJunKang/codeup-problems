# garbage = int(input())

# can = (garbage%10*10 + garbage//10)*2

# if can <= 50:
#     print(can)
#     print("GOOD")
# elif 50 < can < 100:
#     print(can)
#     print("OH MY GOD")

# elif 100 < can:
#     can = can%100
#     if can <=50:
#         print(can)
#         print("GOOD")
#     else:
#         print(can)
#         print("OH MY GOD")

num = int(input())
num = (num // 10 + (num % 10) * 10) * 2
num = num % 100

print(num)
if num <= 50:
    print("GOOD")
else:
    print("OH MY GOD")