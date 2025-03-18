import sys
sys.stdin = open("input.txt", 'r')


def dp(percent, mask=0, row=0, memo=None):
    if memo is None:
        memo = {}

    if (mask, row) in memo:
        return memo[(mask, row)]

    if row == len(percent):
        return 1

    max_prob = 0
    for col in range(len(percent)):
        if not (mask & (1 << col)):  # col이 선택되지 않았을 때
            new_mask = mask | (1 << col)  # 이전에 선택된 열 + 현재 선택한 열
            prob = percent[row][col] / 100 * dp(percent, new_mask, row + 1, memo)
            max_prob = max(max_prob, prob)

    memo[(mask, row)] = max_prob
    return max_prob


T = int(input())

for t in range(1, T + 1):
    N = int(input())
    percent = [list(map(int, input().split())) for _ in range(N)]

    max_prob = dp(percent) * 100
    print(f"#{t} {max_prob:.6f}")
