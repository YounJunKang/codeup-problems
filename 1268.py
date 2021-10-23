from typing import Counter


n = input()
nums = list(map(int, input().split()))

count = 0
for x in nums:
    if x%2 ==0:
        count = count + 1
        
#int(x/x)

print(count)