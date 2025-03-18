import sys
sys.stdin = open("input.txt", 'r')


def dfs(cnt, height):
    global min_difference
    if height >= B:
        min_difference = min(min_difference, height - B)
        return
    if height - B > min_difference:
        return
    if cnt == N:
        return

    dfs(cnt + 1, height + arr[cnt])  # 포함
    dfs(cnt + 1, height)  # 포함 안함


T = int(input())

for t in range(1, T + 1):
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))
    min_difference = float('inf')

    dfs(0, 0)
    print(f"#{t} {min_difference}")