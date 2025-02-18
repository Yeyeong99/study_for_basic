import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())

    flies = [list(map(int, input().split())) for _ in range(N)]

    max_flies = -float('inf')
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            num_flies = 0
            for m in range(M):
                num_flies += sum(flies[i + m][j: j + M])

            max_flies = max(max_flies, num_flies)

    print(f"#{t} {max_flies}")