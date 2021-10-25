n = int(input())
nums = list(map(int, input().split()))

s = 0

for x in nums:
    if x%2 == 0:
        s = s+1

print(s)