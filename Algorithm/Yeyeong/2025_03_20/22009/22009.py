import sys, heapq
sys.stdin = open("input.txt", 'r')


def prim(start_node):
    pq = [(0, start_node)]
    mst = [0] * (V + 1)

    min_weight = 0

    while pq:
        weight, node = heapq.heappop(pq)

        if mst[node]:
            continue

        mst[node] = 1
        min_weight += weight

        for next_node in range(V + 1):
            if graph[node][next_node] == 0:
                continue

            if mst[next_node]:
                continue

            heapq.heappush(pq, (graph[node][next_node], next_node))
    return min_weight


T = int(input())

for t in range(1, T + 1):
    V, E = map(int, input().split())
    graph = [[0] * (V + 1) for _ in range(V + 1)]

    for _ in range(E):
        s, e, w = map(int, input().split())
        graph[s][e] = w
        graph[e][s] = w

    print(f"#{t} {prim(0)}")