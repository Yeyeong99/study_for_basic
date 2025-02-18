import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for t in range(1, T + 1):
    word1 = input()
    word2 = input()

    result = 1 if word1 in word2 else 0

    print(f"#{t} {result}")
