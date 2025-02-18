import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    num_list = [i for i in range(1, N ** 2 + 1)]
    snail = [[0 for i in range(N)] for j in range(N)]

    # 1954 이중 배열의 인덱스를 가리킬 i, j
    # num_list에서 숫자를 찾아올 인덱스 k
    i = 0
    j = 0
    k = 0
    while True:
        snail[i][j] = num_list[k]
        if num_list[k] == N ** 2:
            break

        if j < (N - 1) and snail[i][j + 1] == 0:
            if i > 0 == snail[i - 1][j]:
                i -= 1
            else:
                j += 1
        elif i < (N - 1) and snail[i + 1][j] == 0:
            i += 1
        elif j > 0 == snail[i][j - 1]:
            j -= 1
        elif i > 0 == snail[i - 1][j]:
            i -= 1

        k += 1

    print(f"#{t}")
    for line in snail:
        print(' '.join(map(str, line)))
