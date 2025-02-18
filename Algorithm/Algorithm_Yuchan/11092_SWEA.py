T = int(input())
for test_case in range(1, T + 1):

    N = int(input())
    arr = list(map(int, input().split()))

    max_list = []
    min_list = []

    for i in range(N):
        if max(arr) == arr[i]:
            max_list.append(i)
        if min(arr) == arr[i]:
            min_list.append(i)

    print(f'#{test_case} {abs(max(max_list) - (min(min_list)))}')
