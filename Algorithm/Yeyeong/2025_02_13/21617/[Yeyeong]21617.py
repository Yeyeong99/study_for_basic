import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for t in range(1, T + 1):
    input_data = input()
    stack = []

    open_bracket = ['{', '(']
    close_bracket = ['}', ')']

    result = 1
    if input_data[0] in close_bracket:
        result = 0
    else:
        for data in input_data:
            if data in open_bracket:
                stack.append(data)
            elif data in close_bracket:
                if len(stack) == 0:
                    result = 0
                    break
                else:
                    pop_data = stack.pop()
                    if (pop_data == '{' and data == '}') or (pop_data == '(' and data == ')'):
                        continue
                    else:
                        result = 0
                        break
            else:
                continue
    if len(stack) != 0:
        result = 0

    print(f"#{t} {result}")