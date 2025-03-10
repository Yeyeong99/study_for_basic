import sys
sys.stdin = open('input (4).txt', 'r')
sys.stdout = open('output.txt', 'w')

def overhand(arr):

    return arr[len(arr)-int(len(arr)*0.37):] + arr[:len(arr)-int(len(arr)*0.37)]

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
    N, S = list(map(int, input().split()))

    card_list = []
    for i in range(N):
        card_list.append(str(i+1))

    for _ in range(S):
        card_list = perfect(overhand(card_list))

    print(f'#{tc}', *card_list)

