import sys
sys.stdin = open('sample_input (2).txt', 'r')
sys.stdout = open('output.txt', 'w')

def get_code(arr):

    hex_code_list = []
    for row in arr:
        hex_code
        for num in row:
            if num != 0:
                row

#
#     # for i in range(N):
#     #     hex_code = ''
#     #     for j in range(N):
#     #         if arr[i][j] != 0:
#     #             if arr[i][j].isdigit():
#     #                 hex_code += arr[i][j]
#     #
#     #     if hex_code not in hex_code_list:
#     #         hex_code_list.append(hex_code)
#
#

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(str, input().strip())) for _ in range(N)]

    get_code(arr)



# char = '1DB176C588D26EC'
# lst = list(char)
# result = ''
# for i in range(len(char)):
#     if char[i].isdigit():
#         result += bin(int(char[i]))[2:].zfill(4)
#     else:
#         result += bin(int(char[i], 16))[2:]
#
# print(result)


# A = [0,0,0,1,1,0,1,0,0,]
# B = ''.join(map(str, A))
# C = B.lstrip('0')
# print(C)