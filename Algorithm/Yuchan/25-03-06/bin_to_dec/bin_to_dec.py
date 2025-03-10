# import sys
# sys.stdin = open('start_input.txt', 'r')
# sys.stdout = open('start_output.txt', 'w')

def bin_to_dec(target):

    new_arr = []
    for row in target:
        new_arr += row

    dec_list = []
    for i in range(0, N*10, 7):
        bin_list = new_arr[i:i+7][::-1]
        num = 0
        for j in range(len(bin_list)):
            if bin_list[j] == 1:
                num += 2 ** j
        dec_list.append(num)

    return dec_list

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().strip())) for _ in range(N)]

    print(f'#{tc} {" ".join((map(str, bin_to_dec(arr))))}')

