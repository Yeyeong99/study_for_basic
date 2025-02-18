import sys
sys.stdin = open("input.txt", "r")

T = 10

for t in range(1, T + 1):
    N, input_data = input().split()
    N = int(N)
    input_data = list(map(int, input_data))

    stack = [input_data[0]]
    top = 0
    for i in range(1, N):
        if len(stack) == 0:
            top += 1
            stack.append(input_data[i])
        elif stack[top] != input_data[i]:
            top += 1
            stack.append(input_data[i])
        elif stack[top] == input_data[i]:
            top -= 1
            stack.pop()

    print(f"#{t} {''.join(map(str,stack))}")