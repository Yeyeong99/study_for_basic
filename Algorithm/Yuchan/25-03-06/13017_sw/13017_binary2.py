import sys
sys.stdin = open('sample_input(18) (1).txt', 'r')
sys.stdout = open('output.txt', 'w')

def get_bin(num):
    bin = '0.'
    while num > 0:
        num *= 2
        number = int(num)
        bin += str(number)
        num -= number

        if len(bin) > 15:
            return 'overflow'

    return bin[2:]

T = int(input())
for tc in range(1, T + 1):
    N = input()

    print(f'#{tc} {get_bin(float(N))}')



