import sys
sys.stdin = open("input.txt", 'r')


def dfs(idx, cnt):
    global min_change
    if cnt >= min_change:  # 백트래킹: 최소 교체 횟수보다 크면 종료
        return
    if idx >= N - 1:  # 목적지 도착 시 최소 교체 횟수 갱신
        min_change = min(min_change, cnt)
        return
    if idx == N:
        return

    dfs(idx + 1, cnt + data[idx])
    dfs(idx + 1, cnt)


T = int(input())

for t in range(1, T + 1):
    data = list(map(int, input().split()))
    N = data[0]

    min_change = float('inf')
    dfs(1, -1)
    print(f"#{t} {min_change}")