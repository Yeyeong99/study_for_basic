import sys
sys.stdin = open("input.txt", 'r')


def find_set(x):
    if parent[x] != x:
        parent[x] = find_set(parent[x])
    return parent[x]


def union(x, y):
    rx = find_set(x)
    ry = find_set(y)

    if rx != ry:
        parent[ry] = rx


T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    relation = list(map(int, input().split()))

    people = list(range(1, N + 1))
    parent = list(range(N + 1))
    teams = []

    for i in range(M):
        teams.append((relation[i * 2], relation[i * 2 + 1]))

    for team in teams:
        union(team[0], team[1])

    result = set()
    for i in range(N + 1):
        result.add(find_set(i))

    print(f"#{t} {len(result) - 1}")
