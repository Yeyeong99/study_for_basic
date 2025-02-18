import sys
sys.stdin = open("input.txt", "r")

T = 10

for t in range(1, T + 1):
    tc, N = map(int, input().split())
    stations = list(map(int, input().split()))
    stations_num = 100
    lines = {i: [] for i in range(stations_num)}

    for s in range(len(stations) - 1):
        if s % 2 == 0:
            lines[stations[s]].append(stations[s + 1])

    visited = [0] * stations_num
    stack = [0]

    result = 0
    while stack:
        station = stack.pop()
        if station == 99:
            result = 1
            break
        if not visited[station]:
            visited[station] = 1
            stack += lines[station]

    print(f"#{tc} {result}")
