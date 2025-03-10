for test_case in range(1, 11):

    T = int(input())
    arr = list(map(int, input().split()))

    arr.sort()
    for i in range(T):
        arr[0] += 1
        arr[-1] -= 1
        arr.sort()

    print(f'#{test_case} {arr[-1] - arr[0]}')

