import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for t in range(1, T + 1):
    area = [[[] for _ in range(10)] for _ in range(10)]
    N = int(input())

    colors = [list(map(int, input().split())) for _ in range(N)]
    result = 0

    for color in colors:
        for i in range(color[0], color[2] + 1):
            for j in range(color[1], color[3] + 1):
                area[i][j].append(color[4])

    for i in range(10):
        for j in range(10):
            if (1 in area[i][j]) and (2 in area[i][j]):
                result += 1

    print(f"#{t} {result}")
