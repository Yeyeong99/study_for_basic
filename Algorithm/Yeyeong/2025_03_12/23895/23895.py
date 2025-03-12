import sys
sys.stdin = open("input.txt", 'r')


def dfs(current_location, visited_count, battery_used):
    global min_battery_usage

    # 모든 관리 구역을 방문한 경우
    if visited_count == N - 1:
        min_battery_usage = min(min_battery_usage, battery_used + battery_cost[current_location][0])  # 사무실(0)로 복귀
        return

    # 가지치기: 현재 소비량이 이미 최소값보다 크다면 탐색 중단
    if battery_used >= min_battery_usage:
        return

    for next_location in range(1, N):  # 1번(사무실)은 제외하고 방문
        if not visited[next_location]:  # 방문하지 않은 구역 탐색
            visited[next_location] = True
            dfs(next_location, visited_count + 1, battery_used + battery_cost[current_location][next_location])
            visited[next_location] = False  # 백트래킹


T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    battery_cost = [list(map(int, input().split())) for _ in range(N)]
    min_battery_usage = float('inf')

    visited = [False] * N  # 방문 여부 체크 리스트
    visited[0] = True  # 사무실(0번) 방문 처리 후 시작
    dfs(0, 0, 0)  # 현재 위치: 사무실(0), 방문한 개수: 0, 배터리 사용량: 0

    print(f"#{test_case} {min_battery_usage}")