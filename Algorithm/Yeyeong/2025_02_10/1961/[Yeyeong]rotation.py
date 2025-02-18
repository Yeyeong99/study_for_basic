import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for t in range(1, T + 1):
    N = int(input())

    num_list = [list(map(int, input().split())) for i in range(N)]

    rotation_90 = list(zip(*num_list[::-1]))
    rotation_180 = list(zip(*rotation_90[::-1]))
    rotation_270 = list(zip(*rotation_180[::-1]))

    print(f"#{t}")
    for i, j, k in zip(rotation_90, rotation_180, rotation_270):
        i = map(str, i)
        j = map(str, j)
        k = map(str, k)

        print(''. join(i), ''.join(j), ''.join(k))
