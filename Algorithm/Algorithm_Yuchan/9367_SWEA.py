T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    max_carrot = 1
    counter = 1
    for i in range(1, N):
        if arr[i-1] < arr[i]:
            counter += 1
            max_carrot = max(max_carrot, counter)
        else:
            counter = 1

    print(f'#{test_case} {max_carrot}')

