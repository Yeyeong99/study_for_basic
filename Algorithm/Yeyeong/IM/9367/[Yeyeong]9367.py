import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    sizes = list(map(int, input().split()))

    count = 1
    max_num = 1
    for i in range(1, N):
        if sizes[i] > sizes[i - 1]:
            count += 1
            max_num = max(max_num, count)
        else:
            count = 1

    print(f"#{t} {max_num}")
