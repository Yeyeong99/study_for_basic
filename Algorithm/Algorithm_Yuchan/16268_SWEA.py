T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_sum = 0

    for i in range(N):
        for j in range(M):
            cross_sum = arr[i][j]

            if i > 0:
                cross_sum += arr[i - 1][j]
            if i < N - 1:
                cross_sum += arr[i + 1][j]
            if j > 0:
                cross_sum += arr[i][j - 1]
            if j < M - 1:
                cross_sum += arr[i][j + 1]

            max_sum = max(max_sum, cross_sum)

    print(f'#{test_case} {max_sum}')
