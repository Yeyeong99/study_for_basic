import sys
sys.stdin = open("input.txt", "r", encoding='UTF8')

T = 10

for t in range(1, T + 1):
    t_case = input()
    find_txt = input()
    txt = input()

    print(f"#{t} {txt.count(find_txt)}")
