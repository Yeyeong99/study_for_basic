T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    left_right_count = 0
    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[i][j] == 1:
                cnt += 1
            if arr[i][j] == 0:
                if cnt == K:
                    left_right_count += 1
                cnt = 0
        if cnt == K:
            left_right_count += 1

    up_down_count = 0
    for j in range(N):
        cnt = 0
        for i in range(N):
            if arr[i][j] == 1:
                cnt += 1
            if arr[i][j] == 0:
                if cnt == K:
                    up_down_count += 1
                cnt = 0
        if cnt == K:
            up_down_count += 1

    print(f'#{test_case} {up_down_count+left_right_count}')
