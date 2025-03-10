# for test_case in range(1, 11):
#     N = int(input())
#     arr = [list(input().strip()) for _ in range(8)]
#
#     # 가로 회문 확인
#     row_counter = 0
#     for i in range(8):
#         for j in range(8):
#             if j + N - 1 < 8:
#                 if arr[i][j] == arr[i][j + N - 1]:
#                     if arr[i][j:j+N] == arr[i][j:j+N][::-1]:
#                         row_counter += 1
#
#     # 세로 회문 확인
#     col_counter = 0
#     for j in range(8):
#         col_list = []
#         for i in range(8):
#             col_list.append(arr[i][j])
#         for k in range(8):
#             if k + N - 1 < 8:
#                 if col_list[k] == col_list[k+N-1]:
#                     if col_list[k:k+N] == col_list[k:k+N][::-1]:
#                         col_counter += 1
#
#     print(f'#{test_case} {row_counter+col_counter}')
#
#
#

a = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

b = list(map(list,zip(*a)))
print(b)

for row in b:
    print(row)