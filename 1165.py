time, score = input().split()

time = int(time)
score = int(score)

remain = 90 - time

if remain > 0:
    score += 1

if remain % 5 == 0:
    remain -= 1
    
score += remain // 5

print(score)