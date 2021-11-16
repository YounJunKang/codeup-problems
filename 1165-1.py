min, goal = map(int, input().split())

ace = 1

if min%10 != 0:
    ace = ace + (90-min)//5

elif min%10 == 0:
    ace = ace - 1 + (90-min)//5

print(ace + goal)