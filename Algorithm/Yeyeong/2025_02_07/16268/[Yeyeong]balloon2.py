import sys
sys.stdin = open("input.txt", "r")

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

T = int(input())

for t in range(T):
    N, M = map(int, input().split())

    balloons = [[0] * (M + 2)] + [[0] + list(map(int, input().split())) + [0] for n in range(N)] + [[0] * (M + 2)]

    sum_flowers = -float('inf')
    for i in range(1, (N + 1)):
        for j in range(1, (M + 1)):
            sum_balloons = balloons[i][j]
            for nx, ny in zip(dx, dy):
                sum_balloons += balloons[i + nx][j + ny]
            sum_flowers = max(sum_balloons, sum_flowers)

    print(f"#{t + 1} {sum_flowers}")
