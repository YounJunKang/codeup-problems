start = int(input())
days = int(input())
diffs = list(map(int, input().split()))

money = start
for diff in diffs:
    money = money + money * diff / 100

interest = round(money - start)
print(interest)

if interest > 0:
    print("good")
elif interest < 0:
    print("bad")
else:
    print("same")
    