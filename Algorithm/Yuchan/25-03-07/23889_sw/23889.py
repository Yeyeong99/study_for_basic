import sys
sys.stdin = open('hex_dec_input.txt', 'r')
sys.stdout = open('output.txt', 'w')

T = int(input())
for tc in range(1, T + 1):
    arr = list(map(str, input().strip()))

    bin_char = ''
    for i in range(len(arr)):
        if arr[i].isdigit():
            bin_char += bin(int(arr[i]))[2:].zfill(4)
        else:
            bin_char += bin(int(arr[i], 16))[2:]

    N = len(bin_char)
    bin_list = []
    for j in range(0, N, 7):
        bin_list.append(int(bin_char[j:j+7], 2))

    print(f'#{tc}', *bin_list)
