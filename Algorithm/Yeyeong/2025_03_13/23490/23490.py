import sys
sys.stdin = open("input.txt", 'r')


def find_cnt(n):
    global max_cnt
    next_idx = n + 1
    cnt = 1

    while next_idx < N:
        if times[n][1] <= times[next_idx][0]:
            cnt += 1
            n = next_idx

        if next_idx == N - 1:
            max_cnt = max(cnt, max_cnt)

        next_idx += 1


T = int(input())

for t in range(1, T + 1):
    N = int(input())
    times = [list(map(int, input().split())) for n in range(N)]
    times.sort(key=lambda x: (x[1], x[0]))

    max_cnt = -float('inf')
    for tm in range(N):
        find_cnt(tm)

    print(f"#{t} {max_cnt}")
