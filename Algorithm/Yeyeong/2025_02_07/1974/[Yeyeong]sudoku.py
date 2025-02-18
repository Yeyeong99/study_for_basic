import sys
sys.stdin = open("input.txt", "r")


def is_sudoku(arg_list):
    if sorted(arg_list) == [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        return 1
    return 0


T = int(input())

for t in range(1, T + 1):
    lines = [list(map(int, input().split())) for i in range(9)]

    columns = list(map(list, zip(*lines)))

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            square = []
            for r in range(3):
                for q in range(3):
                    square.append(lines[i + r][j + q])
            lines.append(square)
    lines += columns

    result = 0
    for line in lines:
        result += is_sudoku(line)

    if result == 27:
        print(f"#{t} 1")
    else:
        print(f"#{t} 0")
