import sys
sys.stdin = open("input.txt", "r")
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())

    balloons = [list(map(int, input().split())) for n in range(N)]
    max_total = -float('inf')

    for i in range(N):
        for j in range(M):
            flowers = balloons[i][j]
            total = balloons[i][j]  # 풍선 안에 든 꽃잎 수
            for x, y in zip(dx, dy):  # 꽃잎의 수만큼 상하좌우 탐색, 범위 안에 있을 경우만 더함
                for f in range(1, flowers + 1):
                    nx = i + x * f
                    ny = j + y * f
                    if 0 <= nx < N and 0 <= ny < M:  # N * M 행렬이므로 범위를 다르게  설정해야 함
                        total += balloons[nx][ny]
            max_total = max(max_total, total)

    print(f"#{t} {max_total}")