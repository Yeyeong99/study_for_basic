T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    # #오른쪽으로 가기
    # ni = i + di[0]
    # nj = j + dj[0]
    #
    # #아래로 가기
    # ni = i + di[1]
    # nj = j + dj[1]
    #
    # #왼쪽으로 가기
    # ni = i + di[2]
    # nj = j + dj[2]
    #
    # #위로 가기
    # ni = i + di[3]
    # nj = j + dj[3]

    num = 1
    x, y = 0, 0
    direction = 0 # 오른쪽으로 이동

    while num <= N*N:
        arr[x][y] = num
        num += 1

        nx = x + di[direction]
        ny = y + dj[direction]

        if not (0 <= nx < N and 0 <= ny < N) or arr[nx][ny] != 0:
            direction = (direction + 1) % 4
            nx = x + di[direction]
            ny = y + dj[direction]

        x, y = nx, ny

    print(f'#{test_case}')
    for row in arr:
        print(' '.join(map(str, row)))

