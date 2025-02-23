operators = {
    '*': 1,
    '/': 1,
    '+': 2,
    '-': 2
}
t = int(input())
 
for tc in range(1, t + 1):
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
            result.append(e)
     
    while stack:
        result.append(stack.pop())
 
    print(f"#{tc} {''.join(result)}")
