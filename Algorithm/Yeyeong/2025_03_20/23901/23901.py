import sys
sys.stdin = open("input.txt", 'r')


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dijkstra(x, y):
    pq = [(0, x, y)]
    dists = [[INF] * (N) for _ in range(N)]  # 각 정점까지의 최단 거리를 저장하는 리스트
    dists[x][y] = 0  # 시작노드 최단 거리 == 0

    while pq:
        dist, nx, ny = heapq.heappop(pq)

        if dists[nx][ny] < dist:  # 더 작은 경우가 있었다면 제외
            continue

        for next_info in graph[nx][ny]:
            next_dist = next_info[2] - H[nx][ny]
            if next_dist > 0:
                current_dist = dist + next_dist + 1
            else:
                current_dist = dist + 1

            next_x = next_info[0]  # 다음 노드 번호
            next_y = next_info[1]  # 다음 노드 번호

            if dists[next_x][next_y] <= current_dist:  # 이미 같은 가중치거나, 더 작은 가중치를 지나온 적 있으면 continue
                continue

            dists[next_x][next_y] = current_dist

            heapq.heappush(pq, (current_dist, next_x, next_y))
    return dists


import heapq
INF = int(21e8)

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    H = [list(map(int, input().split())) for _ in range(N)]
    graph = [[[] for __ in range(N)] for _ in range(N)]

    for n in range(N):
        for m in range(N):
            for k in range(4):
                r = n + dx[k]
                c = m + dy[k]

                if 0 <= r < N and 0 <= c < N:
                    graph[n][m].append((r, c, H[r][c]))

    cnt = dijkstra(0, 0)[N - 1][N - 1]

    print(f"#{t} {cnt}")
