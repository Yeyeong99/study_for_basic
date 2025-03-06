import sys

sys.stdin = open("input.txt", "r")

T = int(input())

for t in range(1, T + 1):
    N = float(input())
    len_under_0 = str(N).split('.')[1]  # . 을 기준으로 앞 뒤 숫자 저장 뒤에 있는 숫자가 소수점 아래 수

    changed_num = ''
    cnt, i = 0, 1
    while N:
        cnt += 1
        current = 2 ** (-i)
        if N >= current:
            N -= current
            changed_num += '1'
        else:
            changed_num += '0'
        if cnt >= 13:
            changed_num = 'overflow'
        i += 1

    print(f"#{t} {changed_num}")
