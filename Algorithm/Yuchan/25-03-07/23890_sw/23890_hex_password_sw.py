import sys
sys.stdin = open('bit_input.txt', 'r')
sys.stdout = open('output.txt', 'w')

pattern = {
    '001101': 0,
    '010011': 1,
    '111011': 2,
    '110001': 3,
    '100011': 4,
    '110111': 5,
    '001011': 6,
    '111101': 7,
    '011001': 8,
    '101111': 9
}

T = int(input())
for tc in range(1, T + 1):
    arr = list(map(str, input().strip()))

    bin_char = ''
    for i in range(len(arr)):
        if not arr[i].isdigit():
            bin_char += bin(int(arr[i], 16))[2:]
        else:
            bin_char += bin(int(arr[i]))[2:].zfill(4)

    new_bin_char = bin_char.strip('0')
    while len(new_bin_char) % 6 != 0:
        new_bin_char = '0' + new_bin_char

    result = []
    for j in range(0, len(new_bin_char), 6):
        result.append(pattern[new_bin_char[j:j+6]])
    print(f'#{tc}', *result)






