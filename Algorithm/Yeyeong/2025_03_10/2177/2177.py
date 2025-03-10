import sys
sys.stdin = open("input.txt", 'r')

from collections import deque


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 0]


def area(i, j, n):
    queue = deque()
    queue.append((i, j))
    visited = [[False] * N for _ in range(N)]

    while queue:
        x, y = queue.popleft()
        if not visited[x][y]:
            visited[x][y] = True
            for d in range(4):
                for k in range(1, n):
                    nx = x + dx[d] * k
                    ny = y + dy[d] * k

                    if (nx < 0 or nx >= N) or (ny < 0 or ny >= N):
                        continue
                    if (nx, ny) in queue:
                        continue
                    if visited[nx][ny]:
                        continue
                    queue.append((nx, ny))

    result = []
    for p in range(n):
        for q in range(n):
            if visited[p][q]:
                result.append([p, q])

    return result


T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split()) # 도시 크기, 지불 가능 비용
    city = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            for a in range(1, N):
                current = area(i, j, a)
