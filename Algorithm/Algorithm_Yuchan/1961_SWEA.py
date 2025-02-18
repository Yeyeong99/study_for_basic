T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    def turn_90(lst):
        n = len(lst)
        new_list = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                new_list[j][n-i-1] = lst[i][j]
        return new_list

    arr_90 = turn_90(arr)
    arr_180 = turn_90(arr_90)
    arr_270 = turn_90(arr_180)

    print(f'#{tc}')
    for k in range(N):
        print(''.join(map(str, arr_90[k])), ''.join(map(str, arr_180[k])), ''.join(map(str, arr_270[k])))
