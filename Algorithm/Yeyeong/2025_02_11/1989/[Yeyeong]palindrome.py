import sys
sys.stdin = open("input.txt", "r")


def reversed_string(string):
    if len(string) == 0:
        return string
    else:
        s = string[:-1] # 맨 끝을 제외
        return string[-1] + reversed_string(s)


# 재귀로 구현
# T = int(input())
#
# for t in range(1, T + 1):
#     word = input()
#     reversed_word = reversed_string(word)
#
#     result = 1 if word == reversed_word else 0
#
#     print(f"#{t} {result}")

# 구현
T = int(input())

for t in range(1, T + 1):
    word = input()
    result = 1

    for i in range(len(word)):
        if word[i] != word[len(word) - i - 1]:
            result = 0

    print(f"#{t} {result}")