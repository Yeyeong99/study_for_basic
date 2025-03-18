import sys
sys.stdin = open("input.txt", 'r')


def dfs(row, cost):
    global min_cost

    # 현재 비용이 최소 비용보다 크다면 가지치기
    if cost >= min_cost:
        return

    # 모든 제품을 배치한 경우 최소 비용 갱신
    if row == N:
        min_cost = min(min_cost, cost)
        return

    # 각 열(공장)마다 탐색
    for col in range(N):
        if not visited[col]:  # 아직 선택되지 않은 공장이라면
            visited[col] = True
            dfs(row + 1, cost + costs[row][col])
            visited[col] = False  # 백트래킹


T = int(input())

for t in range(1, T + 1):
    N = int(input())
    costs = [list(map(int, input().split())) for _ in range(N)]

    min_cost = float('inf')
    visited = [False] * N  # 각 공장 사용 여부 표시
    dfs(0, 0)

    print(f"#{t} {min_cost}")
    # 31 12 20 12 3 (3 1 4 0 2)
