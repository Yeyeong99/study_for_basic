import sys
sys.stdin = open("input.txt", 'r')

dx = [0, 0, -1, 1]  # 상(0), 하(1), 좌(2), 우(3)
dy = [1, -1, 0, 0]

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    result = 0

    # 좌표 확장 (0.5초 단위 처리)
    for i in range(N):
        data[i][0] = (data[i][0] + 1000) * 2  # x좌표
        data[i][1] = (data[i][1] + 1000) * 2  # y좌표

    for _ in range(8000):  # 최대 4000초 시뮬레이션 (0.5초 단위)
        pos_dict = {}
        active = False

        # 1. 원자 이동
        for i in range(N):
            x, y, d, e = data[i]
            if e == 0:  # 소멸된 원자 건너뛰기
                continue
            active = True

            # 새로운 좌표 계산
            nx = x + dx[d]
            ny = y + dy[d]
            data[i][0] = nx
            data[i][1] = ny

            # 충돌 위치 기록
            key = (nx, ny)
            if key not in pos_dict:
                pos_dict[key] = []
            pos_dict[key].append(i)

        if not active:  # 모든 원자 소멸
            break

        # 2. 충돌 검사
        for key in pos_dict:
            atoms = pos_dict[key]
            if len(atoms) >= 2:
                sum_e = 0
                for idx in atoms:
                    if data[idx][3] > 0:
                        sum_e += data[idx][3]
                        data[idx][3] = 0  # 에너지 방출
                result += sum_e

    print(f"#{t} {result}")
