import sys
sys.stdin = open("input.txt", 'r')


def enq(n):
    global last_idx
    last_idx += 1
    nodes[last_idx] = n

    c = last_idx
    p = c // 2
    while p and nodes[p] > nodes[c]:
        nodes[p], nodes[c] = nodes[c], nodes[p]
        c = p
        p = c // 2


def sum_all(n):
    cnt = 0
    while n > 1:
        cnt += nodes[n // 2]
        n //= 2

    return cnt


T = int(input())

for t in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))
    nodes = [0] * (N + 1)
    last_idx = 0
    for x in numbers:
        enq(x)
    result = sum_all(N)

    print(f"#{t} {result}")
