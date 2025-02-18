import sys

sys.stdin = open("input.txt", "r")

T = int(input())

for t in range(1, T + 1):
    V, E = map(int, input().split())
    lines_list = [list(map(int, input().split())) for e in range(E)]
    S, G = map(int, input().split())

    # 노드와 간선 저장
    lines = {}
    for v in range(1, V + 1):
        lines[v] = []

    for v, e in lines_list:
        if v in lines.keys():
            lines[v].append(e)
        else:
            lines[v] = [e]
    print(lines)

    stack = [S]
    result = 0
    # (1 -> 5) (1 -> 3에서 끊김)
    # 1 -> 3 (0) -> 4 (0)
    while stack:
        current_node = stack.pop()
        # 방문한 노드가 같으면 끝
        if current_node == G:
            result = 1
            break
        # 스택에 아무것도 없을 때 = 방문을 다 함
        elif not stack:
            result = 0

        # 방문해야 하는 노드 스택에 추가
        if lines[current_node]:
            stack += lines[current_node]

    print(f"#{t} {result}")
