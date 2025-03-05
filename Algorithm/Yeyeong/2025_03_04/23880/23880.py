import sys
sys.stdin = open("input.txt", "r")


def inorder(node, i):
    global visited
    if node[i]:
        for j in node[i]:
            inorder(node, j)
            if j not in visited:
                visited += [j]
            if i not in visited:
                visited += [i]


T = 10

for t in range(1, T + 1):
    N = int(input())
    nodes = [[] for _ in range(N + 1)]
    characters = [''] * (N + 1)
    for _ in range(N):
        input_data = input().split()
        idx = int(input_data[0])  # 현재 노드
        character = input_data[1]  # 현재 노드에 해당하는 글자
        characters[idx] = character  # 글자 저장

        if len(input_data) > 2:  # 자식 노드가 있을 경우 저장
            for d in input_data[2:]:
                child = int(d)
                nodes[idx] += [child]

    visited = []
    inorder(nodes, 1)
    result = ''

    for v in visited:
        result += characters[v]

    print(f"#{t} {result}")