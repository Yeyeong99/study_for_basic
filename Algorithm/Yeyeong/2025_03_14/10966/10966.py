import sys
sys.stdin = open("input.txt", 'r')

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def calculate_sum(N, M, grid):
    dist = [[-1] * M for _ in range(N)]
    q = deque()

    # 1. 모든 W를 큐에 추가
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 'W':
                dist[i][j] = 0
                q.append((i, j))

    # 2. BFS로 최단거리 계산
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < M and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))

    # 3. L 칸 거리 합산
    return sum(dist[i][j] for i in range(N) for j in range(M) if grid[i][j] == 'L')


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    grid = [list(input().strip()) for _ in range(N)]
    print(f"#{tc} {calculate_sum(N, M, grid)}")
