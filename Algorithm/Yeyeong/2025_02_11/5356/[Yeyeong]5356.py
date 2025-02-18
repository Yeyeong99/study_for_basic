import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for t in range(1, T + 1):
    words = [list(input()) for _ in range(5)]

    # words 내의 값 중 길이가 가장 긴 경우를 찾음
    # 가장 긴 길이에 맞춰 모든 문자열의 길이를 조절해준다.
    max_length = max([len(word) for word in words])

    for word in words:
        if len(word) < max_length:
            word += '/' * (max_length - len(word))

    # 전치 행렬로 변환 (세로로 읽기 위해)
    columns = list(map(list, zip(*words)))

    result = ''
    # 세로로 변한 문자열을 합쳐주기
    for column in columns:
        for c in column:
            if c != '/':
                result += c

    print(f"#{t} {result}")