n = int(input())

# n개의 줄을 출력시킬꺼다
for x in range(n):
    # x는 0, 1, 2, ..., n-1로 나온다.
    # x는 그 줄의 공백의 수다

    # x번 만큼 공백 출력
    for _ in range(x):
        print(' ', end='')

    # 별은 그 줄에서 n-x만큼 출력
    for _ in range(n-x):
        print('*', end='')

    # 엔터
    print()
