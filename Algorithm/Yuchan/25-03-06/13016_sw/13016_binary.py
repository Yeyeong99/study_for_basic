# import sys
# sys.stdin = open('sample_input(17).txt', 'r')
# sys.stdout = open('output.txt', 'w')

def hex_to_bin(list):

    bin = []
    for i in range(len(list)):
        if str(list[i]).isdigit():
            num = int(list[i])
        else:
            num = hex_dict[list[i]]

        bin_list = []
        while num != 0:
            bin_list.append(num % 2)

            num = num // 2

        while len(bin_list) < 4:
            bin_list.append(0)
        bin_list.reverse()
        bin += bin_list

    return(''.join(map(str, bin)))

T = int(input())
for tc in range(1, T + 1):
    N, H = list(input().split())

    hex_dict = {'A' : 10,
                'B' : 11,
                'C' : 12,
                'D' : 13,
                'E' : 14,
                'F' : 15
                }

    arr = list(H)

    print(f'#{tc} {hex_to_bin(arr)}')
