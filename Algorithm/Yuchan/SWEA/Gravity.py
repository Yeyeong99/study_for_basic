T = int(input())
for test_case in range(1, T + 1):

    N = int(input())
    arr = list(map(int, input().split()))

    max_drop = 0

    for i in range(N):
        drop_counter = 0
        for j in range(i+1, N):
            if arr[j] < arr[i]:
                drop_counter += 1

        max_drop = max(max_drop, drop_counter)

    print(f'#{test_case} {max_drop}')
