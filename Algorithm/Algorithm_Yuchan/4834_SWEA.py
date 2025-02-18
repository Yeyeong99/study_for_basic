T = int(input())
for test_case in range(1, T + 1):

    N = int(input())
    arr = list(map(int, input()))

    count_list = [0] * 10

    for num in arr:
        count_list[num] += 1

    max_count = max(count_list)

    max_num = 0
    for i in range(10):
        if count_list[i] == max_count:
            max_num = i

    print(f'#{test_case} {max_num} {max_count}')
