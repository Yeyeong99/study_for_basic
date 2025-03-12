import sys
sys.stdin = open("input.txt", 'r')

T = int(input())

for t in range(1, T + 1):
    number, cnt = input().split()
    number = list(map(int, number))
    cnt = int(cnt)


