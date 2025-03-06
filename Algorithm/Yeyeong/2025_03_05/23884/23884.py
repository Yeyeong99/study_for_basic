import sys
sys.stdin = open("input.txt", "r")


def postorder(node, i):
    global postorder_equation, visited
    if node[i]:
        for j in node[i]:
            postorder(node, j)
            if j not in visited:
                visited.append(j)
                postorder_equation.append(nodes[j])
        if i not in visited:
            visited.append(i)
            postorder_equation.append(nodes[i])


T = 10

for t in range(1, T + 1):
    N = int(input())
    nodes_info = [[] for _ in range(N + 1)]
    nodes = [''] * (N + 1)

    # 간선 정보 저장
    for i in range(N):
        data = input().split()
        # 숫자일 경우 int로 바꾸어 저장, 아니면 그냥 저장
        nodes[int(data[0])] = int(data[1]) if data[1].isdecimal() else data[1]

        if len(data) > 2:
            for d in data[2:]:
                nodes_info[int(data[0])].append(int(d))

    # 후위표기식으로 바꿔주기
    postorder_equation, visited = [], []
    postorder(nodes_info, 1)

    # 후위표기식 이용해 계산
    compute = []
    operators = ['+', '-', '*', '/']
    for i in range(len(postorder_equation)):
        if postorder_equation[i] in operators:
            second = compute.pop()
            first = compute.pop()
            if postorder_equation[i] == '-':
                compute.append(first - second)
            elif postorder_equation[i] == '+':
                compute.append(first + second)
            elif postorder_equation[i] == '*':
                compute.append(first * second)
            else:
                compute.append(first / second)
        else:
            compute.append(postorder_equation[i])

    print(f"#{t} {int(compute[0])}")


