n = int(input())
nums = list(map(int, input().split()))

sum = 0
for x in nums:
    sum += x

print(sum)

"""

input() => '3 5 7 7 2'
input().split() => ['3', '5', '7', '7', '2']
map(int, input().split()) => 추상체 mapOf([int('3'), int('5'), int('7'), int('7'), int('2')])
list(map(int, input().split())) => [3, 5, 7, 7, 2]

"""