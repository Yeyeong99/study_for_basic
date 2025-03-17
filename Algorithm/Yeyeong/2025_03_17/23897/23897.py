import sys
sys.stdin = open("input.txt", 'r')


def binary_search(left, right, target, direction):
    global cnt
    if left > right:
        return

    mid = (left + right) // 2

    if target == first[mid]:
        cnt += 1
        return

    if target < first[mid]:
        if direction == 'left':
            return 0
        direction = 'left'
        binary_search(left, mid - 1, target, direction)
    else:
        if direction == 'right':
            return 0
        direction = 'right'
        binary_search(mid + 1, right, target, direction)
    return 0


T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    first = sorted(list(map(int, input().split())))
    second = list(map(int, input().split()))
    cnt = 0
    for num in second:
        binary_search(0, N - 1, num, '')
    print(f"#{t} {cnt}")
