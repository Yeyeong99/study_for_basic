T = int(input())
for test_case in range(1, T + 1):
    arr = [list(map(int, input().split())) for _ in range(9)]

    result = 1

    # 가로 탐색
    for row in arr:
        for num in row:
            if row.count(num) > 1:
                result = 0
                break

    # 세로 탐색
    for j in range(9):
        lst = []
        for i in range(9):
            lst.append(arr[i][j])
        for k in range(1, 10):
            if lst.count(k) > 1:
                result = 0
                break

    # 사각형 탐색
    list_1 = []
    for i in range(3):
        for j in range(3):
            list_1.append(arr[i][j])
    for k in range(1, 10):
        if list_1.count(k) > 1:
            result = 0
            break

    list_2 = []
    for i in range(3):
        for j in range(3, 6):
            list_2.append(arr[i][j])
    for k in range(1, 10):
        if list_2.count(k) > 1:
            result = 0
            break

    list_3 = []
    for i in range(3):
        for j in range(6, 9):
            list_3.append(arr[i][j])
    for k in range(1, 10):
        if list_3.count(k) > 1:
            result = 0
            break

    list_4 = []
    for i in range(3, 6):
        for j in range(3):
            list_4.append(arr[i][j])
    for k in range(1, 10):
        if list_4.count(k) > 1:
            result = 0
            break

    list_5 = []
    for i in range(3, 6):
        for j in range(3, 6):
            list_5.append(arr[i][j])
    for k in range(1, 10):
        if list_5.count(k) > 1:
            result = 0
            break

    list_6 = []
    for i in range(3, 6):
        for j in range(6, 9):
            list_6.append(arr[i][j])
    for k in range(1, 10):
        if list_6.count(k) > 1:
            result = 0
            break

    list_7 = []
    for i in range(6, 9):
        for j in range(3):
            list_7.append(arr[i][j])
    for k in range(1, 10):
        if list_7.count(k) > 1:
            result = 0
            break

    list_8 = []
    for i in range(6, 9):
        for j in range(3, 6):
            list_8.append(arr[i][j])
    for k in range(1, 10):
        if list_8.count(k) > 1:
            result = 0
            break

    list_9 = []
    for i in range(6, 9):
        for j in range(6, 9):
            list_9.append(arr[i][j])
    for k in range(1, 10):
        if list_9.count(k) > 1:
            result = 0
            break

    if result == 1:
        answer = 1
    else:
        answer = 0

    print(f'#{test_case} {answer}')

