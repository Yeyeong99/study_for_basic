import sys
# sys.stdin = open('sample_input (2).txt', 'r')
sys.stdout = open('output.txt', 'w')

# get_rhombus 함수에 arr의 좌표를 넣어서 중앙좌표로 지정한 후
# 마름모 안의 1을 다 더하면 집의 수 house_count가 나옴

# (이익) = M * house_count - {K * K + (K - 1) * (K - 1)}
# 위 공식에서 house_count의 최대를 대입해서 이익 = 0 이 되는 손익분기점 K를 먼저 구해서 연산 줄이자.


def get_K(M, house_count):
    k_list = []
    k = 1
    while M * house_count >= (k * k) + (k - 1) * (k - 1):
        k_list.append(k)
        k += 1
    return k_list

def get_rhombus(arr, i, j, N, M):
    max_house = 0

    total_houses = 0
    for row in arr:
        total_houses += sum(row)
    k_list = get_K(M, total_houses)

    for k in reversed(k_list):
        house_count = 0
        for p in range(N):
            for q in range(N):
                if abs(i - p) + abs(j - q) <= (k - 1):
                    house_count += arr[p][q]
        if M * house_count >= (k * k) + (k - 1) * (k - 1):
            if house_count > max_house:
                max_house = house_count

    return max_house

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    for i in range(N):
        for j in range(N):
            house = get_rhombus(arr, i, j, N, M)
            result = max(result, house)

    print(f'#{tc} {result}')


