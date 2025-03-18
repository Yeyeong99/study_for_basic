import sys
sys.stdin = open("input.txt", 'r')


def dfs(i, j, subset, cost):
    global min_cost
    print(subset)

    if cost > min_cost:
        return

    if len(subset) == N:
        min_cost = min(min_cost, cost)
        return

    if visited_column[j]:
        dfs(i, (j + 1) % N, subset, cost)
    else:
        visited_column[j] = 1
        dfs(i + 1, j, subset + [j], cost + products[i][j])
        visited_column[j] = 0


T = int(input())

for t in range(1, T + 1):
    N = int(input())
    products = [list(map(int, input().split())) for _ in range(N)]
    min_cost = float('inf')
    visited_column = [0] * N
    for c in range(N):
        dfs(0, c, [], 0)
    print(min_cost)

    # 31 12 20 12 3 (3 1 4 0 2)