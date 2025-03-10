T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    for i in range(N-1):
        for j in range(i+1, N):
            if arr[i] >= arr[j]:
                arr[j], arr[i] = arr[i], arr[j]

    print(f'#{test_case}', *arr)

