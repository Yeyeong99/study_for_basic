# from collections import deque
#
# T = int(input())
#
# for tc in range(1, T + 1):
#     N, M, R, C, L = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
#     di = [-1, 1, 0, 0]
#     dj = [0, 0, -1, 1]
#
#     q = deque([(R, C, 1)])
#
#     visited = [[0] * M for _ in range(N)]
#
#     group_1 = [1, 2, 3, 4, 5, 6, 7]
#     group_2 = [1, 2, 4, 5, 6, 7]
#     group_3 = [1, 3, 4, 5, 6, 7]
#     group_4 = [1, 2, 3, 4, 5, 6, 7]
#     group_5 = [1, 2, 3, 4, 5, 6, 7]
#     group_6 = [1, 2, 3, 4, 5, 6, 7]
#     group_7 = [1, 2, 3, 4, 5, 6, 7]
#
#     visited[R][C] = 1
#
#     while q:
#         ci, cj, dist = q.popleft()
#
#         if dist >= L:
#             break
#
#         if arr[ci][cj] == 1:
#             for k in range(4):
#                 ni = ci + di[k]
#                 nj = cj + dj[k]
#                 if 0 <= ni < N and 0 <= nj < M:
#                     if arr[ni][nj] in group_1 and not visited[ni][nj]:
#                         q.append((ni, nj, dist + 1))
#                         visited[ni][nj] = dist + 1
#         if arr[ci][cj] == 2:
#             for k in range(2):
#                 ni = ci + di[k]
#                 nj = cj + dj[k]
#                 if 0 <= ni < N and 0 <= nj < M:
#                     if arr[ni][nj] in group_2 and not visited[ni][nj]:
#                         q.append((ni, nj, dist + 1))
#                         visited[ni][nj] = dist + 1
#         if arr[ci][cj] == 3:
#             for k in range(2, 4):
#                 ni = ci + di[k]
#                 nj = cj + dj[k]
#                 if 0 <= ni < N and 0 <= nj < M:
#                     if arr[ni][nj] in group_3 and not visited[ni][nj]:
#                         q.append((ni, nj, dist + 1))
#                         visited[ni][nj] = dist + 1
#         if arr[ci][cj] == 4:
#             for k in range(0, 4, 3):
#                 ni = ci + di[k]
#                 nj = cj + dj[k]
#                 if 0 <= ni < N and 0 <= nj < M:
#                     if arr[ni][nj] in group_4 and not visited[ni][nj]:
#                         q.append((ni, nj, dist + 1))
#                         visited[ni][nj] = dist + 1
#         if arr[ci][cj] == 5:
#             for k in range(1, 4, 2):
#                 ni = ci + di[k]
#                 nj = cj + dj[k]
#                 if 0 <= ni < N and 0 <= nj < M:
#                     if arr[ni][nj] in group_5 and not visited[ni][nj]:
#                         q.append((ni, nj, dist + 1))
#                         visited[ni][nj] = dist + 1
#         if arr[ci][cj] == 6:
#             for k in range(1, 3):
#                 ni = ci + di[k]
#                 nj = cj + dj[k]
#                 if 0 <= ni < N and 0 <= nj < M:
#                     if arr[ni][nj] in group_6 and not visited[ni][nj]:
#                         q.append((ni, nj, dist + 1))
#                         visited[ni][nj] = dist + 1
#         if arr[ci][cj] == 7:
#             for k in range(0, 3, 2):
#                 ni = ci + di[k]
#                 nj = cj + dj[k]
#                 if 0 <= ni < N and 0 <= nj < M:
#                     if arr[ni][nj] in group_7 and not visited[ni][nj]:
#                         q.append((ni, nj, dist + 1))
#                         visited[ni][nj] = dist + 1
#
#     counter = 0
#     for row in visited:
#         for num in row:
#             if num != 0:
#                 counter += 1
#
#     print(counter)
#
#


from collections import deque

T = int(input())

for tc in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    di = [-1, 1, 0, 0]  # 상하좌우
    dj = [0, 0, -1, 1]

    q = deque([(R, C, 1)])  # (현재 x, 현재 y, 거리 값)
    visited = [[0] * M for _ in range(N)]
    visited[R][C] = 1  # 시작점 방문

    while q:
        ci, cj, dist = q.popleft()  # 현재 위치 및 거리

        # L시간이 지나면 종료
        if dist >= L:
            continue

        # 현재 터널 모양에 따라 이동할 수 있는 방향 결정
        if arr[ci][cj] == 1:
            move_directions = [0, 1, 2, 3]  # 상하좌우
        elif arr[ci][cj] == 2:
            move_directions = [0, 1]  # 상하
        elif arr[ci][cj] == 3:
            move_directions = [2, 3]  # 좌우
        elif arr[ci][cj] == 4:
            move_directions = [0, 3]  # 상우
        elif arr[ci][cj] == 5:
            move_directions = [1, 3]  # 하우
        elif arr[ci][cj] == 6:
            move_directions = [1, 2]  # 하좌
        elif arr[ci][cj] == 7:
            move_directions = [0, 2]  # 상좌
        else:
            move_directions = []

        for k in move_directions:
            ni, nj = ci + di[k], cj + dj[k]

            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0:
                # 다음 위치가 현재 방향과 연결될 수 있는지 확인
                if k == 0 and arr[ni][nj] in [1, 2, 5, 6]:  # 상 (아래로 연결되는 터널)
                    q.append((ni, nj, dist + 1))
                    visited[ni][nj] = dist + 1
                elif k == 1 and arr[ni][nj] in [1, 2, 4, 7]:  # 하 (위로 연결되는 터널)
                    q.append((ni, nj, dist + 1))
                    visited[ni][nj] = dist + 1
                elif k == 2 and arr[ni][nj] in [1, 3, 4, 5]:  # 좌 (오른쪽으로 연결되는 터널)
                    q.append((ni, nj, dist + 1))
                    visited[ni][nj] = dist + 1
                elif k == 3 and arr[ni][nj] in [1, 3, 6, 7]:  # 우 (왼쪽으로 연결되는 터널)
                    q.append((ni, nj, dist + 1))
                    visited[ni][nj] = dist + 1

    # 방문한 위치 개수 세기
    counter = sum(1 for row in visited for num in row if num != 0)
    print(counter)
