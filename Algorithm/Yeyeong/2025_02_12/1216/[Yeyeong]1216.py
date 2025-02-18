import sys
sys.stdin = open("input.txt", "r")


def count_palindromes(arr, n):
    max_length = 1  # 최소 길이 1인 회문도 포함되므로 1로 초기화

    # 각 행에 대해 회문 검사
    for r in range(n):
        for i in range(n):
            for j in range(n, i, -1):  # 긴 길이부터 검사 (가장 긴 회문 찾기 위해)
                tmp_txt = arr[r][i:j]
                # 회문 확인
                if tmp_txt == tmp_txt[::-1]:
                    max_length = max(max_length, len(tmp_txt))

    return max_length


T = 10

for t in range(1, T + 1):
    t_case = int(input())

    N = 100
    texts_row = [list(input()) for _ in range(N)]  # 주어진 100 * 100 받음
    texts_col = list(map(list, (zip(*texts_row))))  # 세로를 판단하기 위해 전환
    texts_row_max = count_palindromes(texts_row, N)
    texts_col_max = count_palindromes(texts_col, N)

    print(f"#{t_case} {max(texts_row_max, texts_col_max)}")