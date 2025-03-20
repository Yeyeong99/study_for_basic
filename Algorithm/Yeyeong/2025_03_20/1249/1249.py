import sys
sys.stdin = open("input.txt", 'r')


def find_set(x):
    if x == parents[x]:
        return x
    parents[x] = find_set(parents[x])
    return parents[x]


def union(x, y):
    ref_x = find_set(x)
    ref_y = find_set(y)

    if ref_x == ref_y:
        return

    if ref_x < ref_y:
        parents[ref_y] = ref_x
    else:
        parents[ref_x] = ref_y


T = int(input())

for t in range(1, T + 1):
    N = int(input())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    E = float(input())

    # 모든 간선에 대해 가중치 계산
    edges = []
    for i in range(N):
        for j in range(i + 1, N):
            environment_cost = E * (((x[i] - x[j]) ** 2) + ((y[i] - y[j]) ** 2))
            edges.append((i, j, environment_cost))

    edges.sort(key=lambda k: k[2])

    parents = [i for i in range(N)]
    cnt = 0
    result = 0

    for u, v, w in edges:
        if find_set(u) != find_set(v):
            union(u, v)
            cnt += 1

            result += w

            if cnt == N - 1:
                break
    print(f"#{t} {round(result)}")

