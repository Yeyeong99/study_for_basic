def rotation(x):
    total = []
    for i in range(n):
        answer = []
        for j in range(n - 1, -1, -1):
            answer.append(str(x[j][i]))
        total.append(answer)
    return total

T = int(input())
for t in range(T):
    n = int(input())
    num_list = [list(map(int, input().split())) for i in range(n)]

    answers = []
    input_data = num_list
    for i in range(3):
        rotated_data = rotation(input_data)
        answers.append(rotated_data)
        input_data = rotated_data
    print(f"#{t+1}")
    for k in range(n):
        for t in range(3):
            print(''.join(answers[t][k]), end=' ')
        print()
