import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for t in range(1, T + 1):
    input_data = input()
    size = len(input_data)
    stack = [0] * size

    top = -1
    result = 1

    if input_data[0] == ')':
        result = -1
    else:
        for data in input_data:
            if data == '(':
                top += 1
                stack[top] = data
            elif data == ')':
                top -= 1

    if top > -1:
        result = -1

    print(f"#{t} {result}")