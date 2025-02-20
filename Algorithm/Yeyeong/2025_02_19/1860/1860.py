import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for t in range(1, T + 1):
    N, M, K = map(int, input().split())  # 예약자 N명, M초 K개 붕어빵
    seconds = list(map(int, input().split()))
    seconds.sort()

    result = 'Possible'
    if seconds[0] < M:
        result = 'Impossible'
    else:
        cnt = 0  # 붕어빵 수
        for i in range(seconds[-1] + 1):
            if i and i % M == 0:
                cnt += K
            if i in seconds:
                cnt -= 1
            if cnt < 0:
                result = 'Impossible'
                break

    print(f"#{t} {result}")
