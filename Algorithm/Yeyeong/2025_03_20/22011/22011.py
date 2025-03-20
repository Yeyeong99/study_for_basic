import sys
sys.stdin = open("input.txt", 'r')


def dijkstra(start_node):
    pq = [(0, start_node)]
    dists = [INF] * (V + 1)  # 각 정점까지의 최단 거리를 저장하는 리스트
    dists[start_node] = 0  # 시작노드 최단 거리 == 0

    while pq:
        dist, node = heapq.heappop(pq)

        if dists[node] < dist:  # 더 작은 경우가 있었다면 제외
            continue

        for next_info in graph[node]:
            next_dist = next_info[0]  # 가중치
            next_node = next_info[1]  # 다음 노드 번호

            current_dist = dist + next_dist
            if dists[next_node] <= current_dist:  # 이미 같은 가중치거나, 더 작은 가중치를 지나온 적 있으면 continue
                continue

            dists[next_node] = current_dist
            heapq.heappush(pq, (current_dist, next_node))
    return dists


import heapq
INF = int(21e8)

T = int(input())

for t in range(1, T + 1):
    V, E = map(int, input().split())
    start_node = 0
    graph = [[] for _ in range(V + 1)]  # 인접 리스트

    for _ in range(E):
        s, e, w = map(int, input().split())
        graph[s].append((w, e))

    result = dijkstra(0)[-1]
    print(f"#{t} {result}")
