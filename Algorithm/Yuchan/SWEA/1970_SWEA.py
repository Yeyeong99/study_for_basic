T = int(input())
for test_case in range(1, T + 1):
    arr = list(map(int, input().strip()))

    # 금액 저장하는 리스트
    change_list = [0] * 8
    N = len(arr)

    for i in range(N):
        if N == 2:
            change_list[7] = arr[0]
            if arr[0] >= 5:
                change_list[7] -= 1
                change_list[6] += 1
        elif N == 3:
            change_list[5] = arr[0]
            if arr[0] >= 5:
                change_list[5] -= 1
                change_list[4] += 1
            if arr[1] >= 5:
                change_list[7] = arr[1]
        elif N == 4:
            change_list[3] = arr[0]
            change_list[5] = arr[1]
            change_list[7] = arr[2]
        elif N == 5:
            change_list[1] = arr[0]
            change_list[3] = arr[1]
            change_list[5] = arr[2]
            change_list[7] = arr[3]
        elif N == 6:
            change_list[0] = 2

