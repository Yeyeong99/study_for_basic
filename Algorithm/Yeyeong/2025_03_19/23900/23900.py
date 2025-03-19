import sys
sys.stdin = open("input.txt", 'r')

from collections import deque


def bfs(start, target, cnt):
    queue = deque()
    queue.append((start, target, cnt))

    while queue:
        s, e, cnts = queue.popleft()
        if s == e:
            return cnts

        if s - e >= 10:
            new_e = e + 10

        elif 1 < s - e < 10:
            new_e = e + 1
        queue.append((s, new_e, cnts + 1))

        if e > s * 2:
            new_e = e // 2

        else:
            new_e = e - 1
        queue.append((s, new_e, cnts + 2))


T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    calculation = [1, 1, 2, 10]
    result = bfs(N, M, 0)
    print(result)
