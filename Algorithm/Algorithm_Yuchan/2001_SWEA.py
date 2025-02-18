T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_kill = 0

    for i in range(N-M+1):
        for j in range(N-M+1):
            fly_kill = 0
            for k in range(M):
                for h in range(M):
                    fly_kill += arr[i+k][j+h]
            max_kill = max(max_kill, fly_kill)

    print(f'#{test_case} {max_kill}')
