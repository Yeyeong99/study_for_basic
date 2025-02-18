import sys

sys.stdin = open("input.txt", "r")

dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())

    board = [[0] * N for _ in range(N)]
    board[N // 2 - 1][N // 2 - 1] = 2
    board[N // 2][N // 2] = 2
    board[N // 2][N // 2 - 1] = 1
    board[N // 2 - 1][N // 2] = 1

    for _ in range(M):
        i, j, stone = map(int, input().split())
        i -= 1
        j -= 1
        board[i][j] = stone

        for direction in range(8):
            nr, nc = i + dx[direction], j + dy[direction]
            different_color_count = 0

            while 0 <= nr < N and 0 <= nc < N:
                if board[nr][nc] == 0:
                    break
                elif board[nr][nc] == 3 - stone:
                    different_color_count += 1
                else:
                    while different_color_count > 0:
                        nr -= dx[direction]
                        nc -= dy[direction]
                        board[nr][nc] = stone
                        different_color_count -= 1
                    break
                nr += dx[direction]
                nc += dy[direction]

    black = white = 0
    for r in range(N):
        for c in range(N):
            if board[r][c] == 1:
                black += 1
            elif board[r][c] == 2:
                white += 1
    print(f"#{t} {black} {white}")
