# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())
# 여러 개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, m = map(int, input().split())

    A_list = list(map(int, input().split()))
    B_list = list(map(int, input().split()))

    if n > m:
        A_list, B_list = B_list, A_list
        n, m = m, n

    max_sum = 0
    for i in range(0, n):
        max_sum += A_list[i] * B_list[i]

    for i in range(m - n + 1):
        current_sum = 0
        for j in range(n):
            current_sum += A_list[j] * B_list[i + j]
        max_sum = max(max_sum, current_sum)


    print(f'#{test_case} {max_sum}')



