# 메모리 초과

import sys
sys.stdin = open("input.txt", 'r')

from itertools import permutations


def find_min(perms):
    global min_cnt
    for perm in perms:
        company_customers_home = [company] + perm + [home]
        distance = 0
        for k in range(len(company_customers_home) - 1):
            current = company_customers_home[k]
            next_location = company_customers_home[k + 1]
            distance += abs(next_location[0] - current[0]) + abs(next_location[1] - current[1])
            if distance >= min_distance:
                break
        min_distance = min(min_distance, distance)


T = int(input())

for t in range(1, T + 1):
    N = int(input())
    idx = list(map(int, input().split()))
    company = [idx[0], idx[1]]
    home = [idx[2], idx[3]]
    customers = idx[4:]
    customers_idx = []
    for i, j in zip(customers[::2], customers[1:len(idx):2]):
        customers_idx.append([i, j])

    perms = list(map(list, permutations(customers_idx, len(customers_idx))))

    min_cnt = float('inf')
    find_min(perms)

    print(f"#{t} {min_cnt}")

# dfs 사용


def dfs(x, y, visited, count, distance):
    global min_cnt

    # 모든 고객을 방문한 경우, 집으로 돌아가는 거리 추가
    if count == N:
        distance += abs(home[0] - x) + abs(home[1] - y)
        min_distance = min(min_distance, distance)
        return

    # 모든 고객을 순회
    for i in range(N):
        if not visited[i]:  # 아직 방문하지 않은 고객이면 방문
            visited[i] = True
            nx, ny = customers[i]
            dfs(nx, ny, visited, count + 1, distance + abs(nx - x) + abs(ny - y))
            visited[i] = False  # 백트래킹


T = int(input())

for t in range(1, T + 1):
    N = int(input())
    idx = list(map(int, input().split()))

    # 위치 정보 저장
    company = (idx[0], idx[1])
    home = (idx[2], idx[3])
    customers = [(idx[i], idx[i + 1]) for i in range(4, len(idx), 2)]

    # 초기화
    min_cnt = float('inf')
    visited = [False] * N  # 고객 방문 여부 체크

    # DFS 탐색 시작 (회사에서 출발)
    dfs(company[0], company[1], visited, 0, 0)

    print(f"#{t} {min_cnt}")
