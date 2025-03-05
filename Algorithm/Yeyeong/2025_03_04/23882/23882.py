import sys
sys.stdin = open("input.txt", "r")


def traversal(node, i):
    global distance
    if node[i]:
        for j in node[i]:
            distance += 1
            traversal(node, j)


T = int(input())

for t in range(1, T + 1):
    E, N = map(int, input().split())
    nodes_info = list(map(int, input().split()))
    nodes = [[] for _ in range(E + 2)]
    for i in range(0, len(nodes_info), 2):
        nodes[nodes_info[i]].append(nodes_info[i + 1])

    distance = 1
    traversal(nodes, N)
    print(f"#{t} {distance}")
