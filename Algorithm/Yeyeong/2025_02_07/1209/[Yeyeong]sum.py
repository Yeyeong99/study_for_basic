import sys
sys.stdin = open("input.txt", "r")

for t in range(1, 11):
    n = int(input())
    arrays = [list(map(int, input().split())) for _ in range(100)]

    max_sum = -float('inf')
    for array in arrays:
        max_sum = max(max_sum, sum(array))

    for i in range(100):
        column_sum = 0
        for j in range(100):
            column_sum += arrays[j][i]
        max_sum = max(max_sum, column_sum)

    dia_sum_1 = 0
    idx1 = 0
    idx2 = 0
    while idx1 < 100 and idx2 < 100:
        dia_sum_1 += arrays[idx1][idx2]
        idx1 += 1
        idx2 += 1
    max_sum = max(dia_sum_1, max_sum)

    dia_sum_2 = 0
    idx1 = 0
    idx2 = 99
    while idx1 < 100 and idx2 > -1:
        dia_sum_2 += arrays[idx1][idx2]
        idx1 += 1
        idx2 -= 1
    max_sum = max(dia_sum_2, max_sum)

    print(f"#{t} {max_sum}")
