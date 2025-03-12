import sys
sys.stdin = open("input.txt", 'r')

dx = [0, 1]
dy = [1, 0]


def dfs(i, j, visited, total):
    global min_sum
    if min_sum <= total:
        return
    if (i, j) == (N - 1, N - 1):
        min_sum = min(min_sum, total)
    else:
        for k in range(2):
            nx = i + dx[k]
            ny = j + dy[k]

            if (nx >= N or nx < 0) or (ny >= N or ny < 0):
                continue

            dfs(nx, ny, visited, total + numbers[nx][ny])


T = int(input())

for t in range(1, T + 1):
    N = int(input())
    numbers = [list(map(int, input().split()))for _ in range(N)]
    min_sum = float('inf')
    dfs(0, 0, [], numbers[0][0])

    print(f"#{t} {min_sum}")