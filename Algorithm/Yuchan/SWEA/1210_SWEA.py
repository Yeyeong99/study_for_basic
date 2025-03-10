
for test_case in range(1, 11):
    T = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    di = [1, 0, 0]
    dj = [0, -1, 1]  # 0 : 아래 , 1 : 왼쪽 , 2 : 오른쪽

    for start_j in range(100): # 마지막 값이 2일때 이 start_j 가 목표값
        if arr[0][start_j] == 1:
            i, j = 0, start_j
            visited = [[0] * 100 for _ in range(100)]
            visited[i][j] = 1

            while i < 99:

                i += di[0] # 아래로 쭉쭉 내려가자
                visited[i][j] = 1

                if arr[i][j] == 2:
                    print(f'#{test_case} {start_j}')
                    break

                for k in range(1,3): # 좌 우 먼저 살피기
                    nj = j + dj[k]
                    if 0 <= nj < 100 and arr[i][nj] == 1 and visited[i][nj] == 0:
                        while 0 <= nj < 100 and arr[i][nj] == 1:
                            j = nj
                            visited[i][j] = 1
                            nj += dj[k]
                        break

