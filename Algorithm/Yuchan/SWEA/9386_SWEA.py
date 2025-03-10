T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input()))

    max_count = 0
    count = 0

    for num in arr:
        if num == 1:
            count += 1
            if count > max_count:
                max_count = count
        else:
            count = 0

    print(f'#{test_case} {max_count}')



