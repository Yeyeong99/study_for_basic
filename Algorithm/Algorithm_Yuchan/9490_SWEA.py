T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    max_sum = 0
    for i in range(N):
        for j in range(M):
            flower = arr[i][j]
            splash = flower
            for k in range(4):
                for h in range(1, splash+1):
                    ni = i + (di[k] * h)
                    nj = j + (dj[k] * h)
                    if 0 <= ni < N and 0 <= nj < M:
                        flower += arr[ni][nj]
            max_sum = max(max_sum, flower)

    print(f'#{test_case} {max_sum}')
