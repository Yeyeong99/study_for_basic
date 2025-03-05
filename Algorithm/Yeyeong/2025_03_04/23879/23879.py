
def preorder(nodes, i):
    global result
    result.append(i)

    if nodes[i]:
        for j in nodes[i]:
            preorder(nodes, j)


V = int(input())
nodes = [[] for _ in range(V + 1)]
input_nodes = list(map(int, input().split()))
for i in range(0, len(input_nodes) - 1, 2):
    nodes[input_nodes[i]].append(input_nodes[i + 1])
result = []
preorder(nodes, 1)
print(f"{' '.join(map(str, result))}")


