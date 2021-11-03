n = int(input())
nums = list(map(int, input().split()))

s = 0

for x in nums:
    if x >= s:
        s = x

print(s)