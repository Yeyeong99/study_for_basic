import sys
sys.stdin = open("input.txt", 'r')

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(i, j, string):
    if len(string) == 7:
        possible.append(string)
        return
    for k in range(4):
        nx = i + dx[k]
        ny = j + dy[k]

        if nx >= 4 or nx < 0 or ny < 0 or ny >= 4:
            continue

        dfs(nx, ny, string + matrix[i][j])


T = int(input())

for t in range(1, T + 1):
    matrix = [input().split() for _ in range(4)]
    possible = []

    for x in range(4):
        for y in range(4):
            dfs(x, y, '')

    print(f"#{t} {len(set(possible))}")
