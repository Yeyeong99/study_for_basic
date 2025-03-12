# import sys
# sys.stdin = open("input.txt", 'r')
#
# from collections import deque
#
# dx = [0, 1, 0, -1]
# dy = [1, 0, -1, 0]
#
#
# def bfs(i, j, a):
#     queue = deque()
#     queue.append((i, j))
#     side = [] # 가장자리 좌표 저장
#     result = [(i, j)]
#     while queue:
#         x, y = queue.popleft()
#         for k in range(4):
#             nx = x + dx[k]
#             ny = y + dy[k]
#
#             if (nx == i or ny == j) and len(side) < 4:
#                 queue.append((nx, ny))
#                 side.append((nx, ny))
#             if
#             result.append((nx, ny))
#     return result
#
#
# def get_profit(i, j):
#     global max_profit
#     for a in range(N):
#         current_dia = bfs(i, j, a)
#         cost = len(current_dia)
#         profit = sum([1 for q, p in current_dia if city[q][p] == 1]) * M
#
#         if cost > profit:
#             continue
#         else:
#             max_profit = max(max_profit, profit - cost)
#
#
# T = int(input())
#
# for t in range(1, T + 1):
#     N, M = map(int, input().split())  # 도시 크기, 지불 가능 비용
#     city = [list(map(int, input().split())) for _ in range(N)]
#     total_houses = sum([1 for i in range(N) for j in range(N) if city[i][j] == 1])
#     max_profit = -float('inf')
#     for i in range(N):
#         for j in range(N):
#             if city[i][j] == 1:
#                 get_profit(i, j)
#
#     print(max_profit)
