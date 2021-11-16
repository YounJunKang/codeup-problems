n = int(input())

# 사각형 출력

# n줄
for i in range(1, n+1):
    # 1번째 줄과 n번째 줄은 n개의 * 출력
    if i == 1 or i == n:
        for j in range(n):
            print("*", end ="")
    else:
        # 그 외에는
        # 별 한개
        print('*', end='')
        # 공백 n-2개
        for j in range(n-2):
            print(" ", end='')
        # 별 한개
        print('*', end='')
    print("")
