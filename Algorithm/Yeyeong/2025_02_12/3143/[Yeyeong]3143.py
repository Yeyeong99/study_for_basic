import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for t in range(1, T + 1):
    a, b = input().split()

    a = a.replace(b, '/')

    print(f"#{t} {len(a)}")