import sys
sys.stdin = open("input.txt", 'r')

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


T = int(input())

for t in range(1, T + 1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    i = 0

    same_x = [] # x가 동일선상에 있는 좌표
    same_y = []  # y가 동일선상에 있는 좌표
    for i in range(N):
        for j in range(i + 1, N):
            print(data[i], data[j])
            if data[i][0] == data[j][0]:
                if (data[i][1] > data[j][1] and data[i][2] == 2 and data[j][2] == 3) or (data[i][1] < data[j][1] and data[j][2] == 2 and data[i][2] == 3):  # 이동방향이 좌 or 우
                    same_x.append(data[i])
                    same_x.append(data[j])
            if data[i][1] == data[j][1]:
                if (data[i][0] < data[j][1] and data[i][2] == 0 and data[j][2] == 1) or (data[i][0] > data[j][1] and data[j][2] == 0 and data[i][2] == 1):  # 이동방향이 좌 or 우
                    same_x.append(data[i])
                    same_y.append(data[j])

    print(same_x, same_y)
