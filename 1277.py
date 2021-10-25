n = int(input())
# 40, 233, 23, 111, 2 ,34, 1
#  0     1  2    3  4   5  6
# n == 7
# nums[0] => 40
# nums[n-1] = nums[6] => 1
# nums[n // 2] = nums[3] => 111

# 첫번째꺼 0 - > 40
# 마지막꺼 n-1 -> 1
# 중간꺼 n // 2 -> 111

nums = list(map(int, input().split()))

print(nums[0],nums[n//2], nums[n-1], sep=' ')