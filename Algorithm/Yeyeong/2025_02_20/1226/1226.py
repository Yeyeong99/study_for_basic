import sys
sys.stdin = open("input.txt", 'r')
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(i, j, cnt):
    global visited
    queue = deque()
    queue.append((i, j, cnt))
    visited[i][j] = 1

    while queue:
        x, y, counts = queue.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if nx >= N or nx < 0 or ny < 0 or ny >= N:
                continue
            if visited[nx][ny]:
                continue
            if maze[nx][ny] == '1':
                continue
            if maze[nx][ny] == '3':
                return counts

            visited[nx][ny] = 1
            queue.append((nx, ny, counts + 1))


T = 10

for t in range(1, T + 1):
    tc = int(input())
    N = 16
    maze = [list(input()) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':
                result = bfs(i, j, 0)

    if result is None:
        print(f"#{tc} 0")
    else:
        print(f"#{tc} 1")
