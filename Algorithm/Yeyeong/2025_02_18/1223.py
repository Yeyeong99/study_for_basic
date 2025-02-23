import sys
sys.stdin = open("input.txt", "r")

operators = {
    '*': 1,
    '/': 1,
    '+': 2,
    '-': 2
}

t = 10

for tc in range(1, t + 1):
    num = int(input())
    equation = input()
    result = []
    stack = []
    for e in equation:
        if e in operators.keys():
            if not stack or operators[e] < operators[stack[-1]]:
                stack.append(e)
            else:
                result.append(stack.pop())
                stack.append(e)

        else:
            result.append(int(e))

    while stack:
        result.append(stack.pop())

    result_stack = []
    for e in result:
        if e in operators.keys():
            num_1 = result_stack.pop()
            num_2 = result_stack.pop()
            if e == '*':
                result_stack.append(num_1 * num_2)
            else:
                result_stack.append(num_1 + num_2)
        else:
            result_stack.append(e)

    print(f"#{tc} {result_stack[0]}")
