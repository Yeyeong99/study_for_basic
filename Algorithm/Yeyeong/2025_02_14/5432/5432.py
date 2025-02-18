import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for t in range(1, T + 1):
    cases = list(input())

    stack = []
    result = 0
    for i in range(len(cases)):
        if cases[i] == '(':
            stack.append(cases[i])
        else:  # ')' 인 경우
            # 레이저일 경우 - 바로 앞이 (
            if cases[i - 1] == '(':
                stack.pop()
                result += len(stack)
            else:
                # 레이저가 아닌 경우
                stack.pop()
                result += 1
    print(f"#{t} {result}")








