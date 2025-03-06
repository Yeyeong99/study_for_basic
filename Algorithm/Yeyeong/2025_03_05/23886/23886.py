import sys
sys.stdin = open("input.txt", 'r')

T = int(input())

for t in range(1, T + 1):
    N, M, L = map(int, input().split())
    nodes = [0] * (N + 1)

    for m in range(M):
        idx, value = map(int, input().split())
        nodes[idx] = value

    for n in range(N, 1, -1):
        nodes[n // 2] += nodes[n]

    answer = nodes[L * 2]
    if (L * 2 + 1) < N + 1:
        answer += nodes[L * 2 + 1]

    print(f"#{t} {answer}")