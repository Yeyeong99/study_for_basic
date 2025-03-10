import sys
sys.stdin = open('sample_input (1).txt', 'r')
sys.stdout = open('output.txt', 'w')

def perfect(arr):

    shuffle_list = arr[len(arr) - int(len(arr)*0.5):]
    first_list = arr[:len(arr) - int(len(arr)*0.5)]
    perfect_list = []
    for k in range(N//2):
        perfect_list.append(first_list[k])
        perfect_list.append(shuffle_list[k])

    if len(shuffle_list) < len(first_list):
        perfect_list.append(first_list[-1])

    return perfect_list

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    card_list = list(map(str, input().split()))

    print(f'#{tc}', *perfect(card_list))

