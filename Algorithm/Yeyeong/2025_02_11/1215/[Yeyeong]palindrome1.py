import sys
sys.stdin = open("input.txt", "r")

T = 10

for t in range(1, T + 1):
    N = int(input())

    # 문자열을 받음
    rows = [list(input()) for _ in range(8)]

    # 세로 열을 판단하기 위해 전치
    columns = list(map(list, zip(*rows)))

    result = 0
    for row in rows:
        for i in range(8 - N + 1):
            # i == 0 인 경우 i - 1을 하면 -1이기 때문에 빈 리스트를 반환함 그래서 경우를 나눔
            if i == 0 and row[i: i + N] == row[i + N - 1:: -1]:
                result += 1
            elif row[i: i + N] == row[i + N - 1: i - 1: -1]:
                result += 1
    for column in columns:
        for i in range(8 - N + 1):
            if i == 0 and column[i: i + N] == column[i + N - 1:: -1]:
                result += 1
            elif column[i: i + N] == column[i + N - 1: i - 1: -1]:
                result += 1

    print(f"#{t} {result}")

