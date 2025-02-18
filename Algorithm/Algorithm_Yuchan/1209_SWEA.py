
for test_case in range(1, 10 + 1):
    T = int(input())
    n, m = 100, 100
    arr_2d = [list(map(int, input().split())) for _ in range(n)]

    max_list = []

    for i in range(100):
        width_sum = sum(arr_2d[i])
        length_sum = sum(arr_2d[j][i] for j in range(100))
        max_list.append(width_sum)
        max_list.append(length_sum)

    right_cross_sum = sum(arr_2d[i][i] for i in range(100))
    max_list.append(right_cross_sum)

    left_cross_sum = sum(arr_2d[i][99 - i] for i in range(100))
    max_list.append(left_cross_sum)

    print(f'#{test_case} {max(max_list)}')
