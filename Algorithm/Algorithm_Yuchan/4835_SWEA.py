T = int(input())
for test_case in range(1, T + 1):

    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    sum_list = []

    for i in range(N):
        num_sum = sum(arr[i:M+i])
        sum_list.append((num_sum))

    new_list = sum_list[:N-M+1]

    print(f'#{test_case} {max(new_list)-min(new_list)}')

