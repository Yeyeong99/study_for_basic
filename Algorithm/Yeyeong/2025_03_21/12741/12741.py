import sys
sys.stdin = open("input.txt", 'r')

T = int(input())

for t in range(1, T + 1):
    A, B, C, D = map(int, input().split())

    coin_s = A if A >= C else C
    coin_e = D if D <= B else B
    answer = coin_e - coin_s
    if answer < 0:
        answer = 0

    print(f"#{t} {answer}")