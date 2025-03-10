import sys
sys.stdin = open('input (8).txt', 'r')
sys.stdout = open('output.txt', 'w')

for tc in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    for j in range(N):
        bin_char = ''
        for i in range(N):
            if arr[i][j] != 0:
                bin_char += str(arr[i][j])
        bin_char = bin_char.lstrip('2')
        bin_char = bin_char.rstrip('1')

        bin_list = list(bin_char)
        visited = [0] * len(bin_list)

        for p in range(len(bin_list)):
            if bin_list[p] == '1' and not visited[p]:
                visited[p] = 1
                for q in range(p + 1, len(bin_list)):
                    if bin_list[q] == '1':
                        visited[q] = 1
                        continue
                    if bin_list[q] == '2':
                        result += 1
                        visited[q] = 1
                        break

    print(f'#{tc} {result}')
