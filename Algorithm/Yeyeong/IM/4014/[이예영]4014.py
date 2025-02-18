def count_impossible(arg_list):
    answer = 0
    for row in arg_list:
        for i in range(1, len(row) - 1):
            count = 1
            # if row[i] == max(row):
            #     continue
            if row[i] != row[i - 1]:
                j = 0
                while row[i + j] == row[i + j + 1]:
                    count += 1
                    j += 1
                
                if ((row[i + 1] != -1) and abs(row[i + 1] - row[i]) > 1) or ((row[i - 1] != -1) and (abs(row[i] - row[i - 1]) > 1)):
                    answer += 1
                    break
                    
                elif count < x:
                    if (row[i - 1] > row[i]) or (row[i + count - 1] < row[i + count]):
                        answer += 1
                        break

                elif (count >= x) and (count < 2 * x):
                    if (row[i+ count] - row[i + count - 1] == 1) and (row[i - 1] != -1 and (row[i - 1] - row[i] == 1)):
                        answer += 1
                        break
            
    return answer

T = int(input())

for t in range(T):
    n, x = map(int,input().split())
    num_list = [list(map(int, input().split())) for i in range(n)]

    row_list = [[-1] + num + [-1] for num in num_list]

    t_list = []
    for i in range(n):
        _list = [-1]
        for j in range(n):
            _list.append(num_list[j][i])
        _list.append(-1)
        t_list.append(_list)

    impossible = count_impossible(row_list) + count_impossible(t_list)
    print(f"#{t + 1} {n * 2 - impossible}")
