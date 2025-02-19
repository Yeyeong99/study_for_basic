import sys
sys.stdin = open(r"C:\Users\twony\Desktop\input.txt", "r", encoding="utf-8")

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_count = 0

    for i in range(N):
        for j in range(N):
            x, y = i, j
            search_point = arr[x][y]  # 처음 시작한 위치의 값 저장
            count = 0

            while True:
                lowest_point = float('inf')
                next_x, next_y = -1, -1

                # 네 방향 탐색
                for d in range(4):
                    nx, ny = x + dx[d], y + dy[d]
                    if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] < arr[x][y]:
                        if arr[nx][ny] < lowest_point:
                            lowest_point = arr[nx][ny]
                            next_x, next_y = nx, ny

                # 더 낮은 곳이 없으면 종료
                if next_x == -1:
                    break

                # 이동
                x, y = next_x, next_y
                count += 1

            max_count = max(max_count, count)

    print(f'#{tc} {max_count}')