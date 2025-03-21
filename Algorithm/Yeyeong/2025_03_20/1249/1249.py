# 다익스트라: BFS + 우선순위큐(누적값)
# 갈 수 있는 모든 곳을 후보 리스트에 넣음
# 후보 리스트 중 가장 적은 시간이 걸리는 곳부터 먼저 탐색 => 우선순위큐
# 특정 위치까지 간 거리들을 계속 저장하면서 나아감
# 전체 탐색이 완료되거나, 도착지 좌표에 도달하면 중지
import sys
sys.stdin = open("input.txt", 'r')


import heapq

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def dijkstra():
    dists = [[int(21e8)] * N for _ in range(N)]  # 누적 거리를 담을 것 모든 좌표를 최대값으로
    dists[0][0] = 0

    pq = [(0, 0, 0)]

    while pq:
        dist, y, x = heapq.heappop(pq)

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if nx >= N or nx < 0 or ny < 0 or ny >= N:
                continue

            new_dist = graph[ny][nx] + dists[y][x]

            if dists[ny][nx] <= new_dist:
                continue

            if ny == N - 1 and nx == N - 1:
                return new_dist

            dists[ny][nx] = new_dist
            heapq.heappush(pq, (new_dist, ny, nx))

    return dists[N - 1][N - 1]


T = int(input())

for t in range(1, T + 1):
    N = int(input())
    graph = [list(map(int, input())) for _ in range(N)]

    result = dijkstra()

    print(f"#{t} {result}")