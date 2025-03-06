import sys
sys.stdin = open("input.txt", "r")


def find_code(code, N, M):
    for i in range(N):
        for j in range(M - 1, -1, -1):
            if code[i][j] == '1':
                current = code[i][j - 55: j + 1]
                return current


decipher = {
    '0001101': '0',
    '0011001': '1',
    '0010011': '2',
    '0111101': '3',
    '0100011': '4',
    '0110001': '5',
    '0101111': '6',
    '0111011': '7',
    '0110111': '8',
    '0001011': '9'
}

T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    codes = [input() for _ in range(N)]
    # 시작은 0 또는 1이지만 맨 끝은 항상 1임

    code = find_code(codes, N, M)
    decimal = []
    for x in range(0, 56, 7):
        current_code = code[x: x + 7]
        decimal.append(int(decipher[current_code]))

    odd = 0
    even = 0
    for y in range(8):
        if y % 2 == 0:
            even += decimal[y]
        else:
            odd += decimal[y]
    if (even * 3 + odd) % 10 == 0:
        answer = sum(decimal)
    else:
        answer = 0

    print(f"#{t} {answer}")


