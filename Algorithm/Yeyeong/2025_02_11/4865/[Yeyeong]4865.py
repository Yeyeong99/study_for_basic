import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for t in range(1, T + 1):
    word1 = input()
    word2 = input()

    # word1에 있는 글자를 기준으로
    # word2의 글자를 수 세기
    max_num = -float('inf')
    for w in word1:
        max_num = max(word2.count(w), max_num)

    print(f"#{t} {max_num}")