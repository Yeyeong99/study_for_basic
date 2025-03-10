import sys
sys.stdin = open("input.txt", 'r')

T = int(input())

for t in range(1, T + 1):
    a, b, c = map(int, input().split())

    if a < b < c:
        print(f"#{t} 0")
    else:
        cnt = 0
        while a >= b or b >= c:
            if a >= b:
                a -= 1
                cnt += 1
            if b >= c:
                b -= 1
                cnt += 1

            if a < 1 or b < 1 or c < 1:
                cnt = -1
                break

        print(f"#{t} {cnt}")