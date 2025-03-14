import sys
sys.stdin = open("input.txt", 'r')

tunnel = {
    1: [[-1, 0], [1, 0], [0, -1], [0, 1]],
    2: [[-1, 0], [1, 0]],
    3: [[0, -1], [0, 1]],
    4: [[-1, 0], [0, 1]],
    5: [[1, 0], [0, 1]],
    6: [[1, 0], [0, -1]],
    7: [[-1, 0], [0, -1]]
}

to_top = [1, 2, 5, 6]
to_bottom = [1, 2, 4, 7]
to_left = [1, 3, 4, 5]
to_right = [1, 3, 6, 7]

from collections import deque


def bfs(i, j, cnt):
    queue = deque()
    queue.append((i, j, cnt))
    visited = [[0] * M for _ in range(N)]
    visited[i][j] = 1
    while queue:
        r, c, distance = queue.popleft()
        print(r, c, matrix[r][c])

        if distance == L:
            return sum([visited[i][j] for i in range(N) for j in range(M)])
        current_delta = tunnel[matrix[r][c]]
        for p, q in current_delta:
            nx = r + p
            ny = c + q

            if nx >= N or nx < 0 or ny >= M or ny < 0:
                continue
            if visited[nx][ny]:
                continue
            if matrix[nx][ny] == 0:
                continue
            if [p, q] == [-1, 0] and matrix[nx][ny] not in to_top:
                continue
            elif [p, q] == [1, 0] and matrix[nx][ny] not in to_bottom:
                continue
            elif [p, q] == [0, -1] and matrix[nx][ny] not in to_right:
                continue
            elif [p, q] == [0, 1] and matrix[nx][ny] not in to_left:
                continue
            visited[nx][ny] = 1
            queue.append((nx, ny, distance + 1))


T = int(input())

for t in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    answer = bfs(R, C, 1)
    print(answer)