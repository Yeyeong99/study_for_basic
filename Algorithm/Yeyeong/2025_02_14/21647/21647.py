import sys
sys.stdin = open("input.txt", "r")

widths = [10, 20]


def dfs(total_width, ten, twenty, counts):
    if total_width == 0:
        return counts
    else:
        if total_width >= twenty:
            total_width -= twenty
        else:
            total_width -= ten
        counts += 1
        return dfs(total_width, ten, twenty, counts)


T = int(input())

for t in range(1, T + 1):
    N = int(input())

    result = 0
    stack = []
    # 20 으로 최대한 채우기
    print(dfs(N, 10, 20, 0))

    # 20을 채울 수 있는 방법

