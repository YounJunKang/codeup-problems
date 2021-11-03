n = int(input())
nums = list(map(int, input().split()))

print(nums[0], nums[n//2], nums[n-1], sep=' ')
