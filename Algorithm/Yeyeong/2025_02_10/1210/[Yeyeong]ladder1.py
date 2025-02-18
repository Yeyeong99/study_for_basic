import sys

sys.stdin = open("input.txt", "r")

T = 10 # test case 10으로 고정

for t in range(1, T + 1):
    t_case = int(input()) # 첫 줄은 test case 순서
    original_ladder = [list(map(int, input().split())) for _ in range(100)]

    for j in range(100):
        ladder = [o[:] for o in original_ladder]  # 지나간 길이 바뀌어 있기 때문에 영향을 받지 않기 위해 원본 복사
        i = 0
        start = [str(i), str(j)]

        while True:
            if ladder[i][j] == 2:
                print(f"#{t_case} {start[1]}")
                break
            elif ladder[i][j] == 1:
                ladder[i][j] = -1  # 지나간 길을 -1 로 해서 갈림길에서 뒤로 가는 일이 없게 함
                if j > 0 and ladder[i][j - 1] == 1:
                    j -= 1
                elif j < 99 and ladder[i][j + 1] == 1:
                    j += 1
                elif i < 99 and ladder[i + 1][j] != 0:  # 아래가 2인 경우도 포함해야함
                    i += 1

            else:
                break


