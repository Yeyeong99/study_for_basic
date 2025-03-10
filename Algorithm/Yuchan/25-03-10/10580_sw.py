T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [0] * N
    cnt = 0

    for i in range(N):
        for j in range(i+1, N):
            if arr[i][0] > arr[j][0] and arr[i][1] < arr[j][1] and not visited[i]:
                cnt += 1

            if arr[i][0] < arr[j][0] and arr[i][1] > arr[j][1] and not visited[i]:
                cnt += 1

    print(f'#{tc} {cnt}')
