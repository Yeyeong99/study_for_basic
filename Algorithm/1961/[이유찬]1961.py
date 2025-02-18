# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#
#     for i in range (N)
#     arr = list(map(int, input().split()))
#


my_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    ]


N = len(my_list)
def turn_90(lst):
    new_list = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new_list[j][N-i-1] = lst[i][j]
    return new_list


print(turn_90(turn_90(my_list)))
# print(my_list[0])
# arr = list(map(int, my_list.split)())
# print(arr)

