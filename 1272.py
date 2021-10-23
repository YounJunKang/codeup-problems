import math
a, b = map(int, input().split())

"""
  1   10    2  20    3  30  4 40  5  50
  1    2    3   4    5   6  7  8  9  10
  0.5  1  1.5   2  2.5   3
  1    1    2   2    3   3
"""

s = 0

if a % 2 == 0:
  s += 10 * (a // 2)
  # s = s + 10 * a // 2
else:
  s += math.ceil(a / 2)

if b % 2 == 0:
  s += 10 * (b // 2)
else:
  s += math.ceil(b / 2)

print(s)

# if a != 1:
#      if a%2 == 0:
#          a = 10(a/2)
#      elif a%2 == 1:
#          a = (a+3)/2-1
# else: a = 1


