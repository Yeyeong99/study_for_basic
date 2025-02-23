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
    stack = [0]
    for e in equation:
        if e in operators.keys():
            num_1 = stack.pop()
            num_2 = stack.pop()
            stack.append(num_1 + num_2) 
        else:
            stack.append(int(e))
    

    print(f"#{tc} {sum(stack)}")
