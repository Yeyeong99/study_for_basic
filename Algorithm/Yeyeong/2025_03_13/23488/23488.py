import sys
sys.stdin = open("input.txt", 'r')

T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    luggage = list(map(int, input().split())) # N
    trucks = list(map(int, input().split())) # M

    luggage.sort(reverse=True)
    trucks.sort(reverse=True)

    truck_used = [0] * M
    total = 0
    m = 0
    for n in range(N):
        for m in range(M):
            if luggage[n] > trucks[m]:
                break
            if luggage[n] <= trucks[m] and not truck_used[m]:
                total += luggage[n]
                truck_used[m] = 1
                break
    print(f"#{t} {total}")
