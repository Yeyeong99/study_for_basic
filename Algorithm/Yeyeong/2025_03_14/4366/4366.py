T = int(input())

for t in range(1, T + 1):
    num_2 = input()
    num_3 = input()

    possible_2 = []
    for i in range(len(num_2) - 1, -1, -1):
        if num_2[i] == '1':
            new_num = num_2[:i] + '0' + num_2[i + 1:]
        else:
            new_num = num_2[:i] + '1' + num_2[i + 1:]
        possible_2.append(new_num)
    possible_2_10 = [int(num, 2) for num in possible_2]

    possible_3 = []
    for i in range(len(num_3) - 1, -1, -1):
        if num_3[i] == '1':
            new_num1 = num_3[:i] + '0' + num_3[i + 1:]
            new_num2 = num_3[:i] + '2' + num_3[i + 1:]
        elif num_3[i] == '2':
            new_num1 = num_3[:i] + '0' + num_3[i + 1:]
            new_num2 = num_3[:i] + '1' + num_3[i + 1:]
        else:
            new_num1 = num_3[:i] + '1' + num_3[i + 1:]
            new_num2 = num_3[:i] + '2' + num_3[i + 1:]
        possible_3 += [new_num1, new_num2]
    possible_3_10 = [int(num, 3) for num in possible_3]

    for num in possible_2_10:
        if num in possible_3_10:
            print(f"#{t} {num}")