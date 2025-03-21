import sys
sys.stdin = open("input.txt", 'r')


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(i, j, k, cnt, direction, way):
    global visited, min_cnt
    visited[i][j] = 1

    for d in range(4):
        nx = i + dx[d]
        ny = j + dy[d]

        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        if visited[nx][ny]:
            continue
        if cnt >= min_cnt:
            continue
        if field[nx][ny] == 'Y':
            cnt += 1
            if direction != d:
                if d + direction == 1 or d + direction == 5:
                    cnt += 2
                else:
                    cnt += 1
            min_cnt = min(min_cnt, cnt)

            return

        elif field[nx][ny] == 'T':
            if k > 0:
                k -= 1
                cnt += 1
                visited[nx][ny] = 1
                if direction != d:
                    if d + direction == 1 or d + direction == 5:
                        cnt += 2
                    else:
                        cnt += 1
                dfs(nx, ny, k, cnt, d, way + [[nx, ny]])
                visited[nx][ny] = 0
                cnt -= 1
                if direction != d:
                    if d + direction == 1 or d + direction == 5:
                        cnt -= 2
                    else:
                        cnt -= 1
                k += 1
            else:
                continue
        else:
            visited[nx][ny] = 1
            cnt += 1
            if direction != d:
                if d + direction == 1 or d + direction == 5:
                    cnt += 2
                else:
                    cnt += 1
            dfs(nx, ny, k, cnt, d, way + [[nx, ny]])
            visited[nx][ny] = 0
            if direction != d:
                if d + direction == 1 or d + direction == 5:
                    cnt -= 2
                else:
                    cnt -= 1
            cnt -= 1


T = int(input())

for t in range(1, T + 1):
    N, K = map(int, input().split())
    field = [list(input()) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]

    min_cnt = float('inf')
    for p in range(N):
        for q in range(N):
            if field[p][q] == 'X':
                dfs(p, q, K, 0, 0, [])  # 좌표, 나무 벨 수 있는 수, 조작 몇 번 했는지, 지금 보고 있는 방향
    if min_cnt == float('inf'):
        min_cnt = -1
    print(f"#{t} {min_cnt}")
