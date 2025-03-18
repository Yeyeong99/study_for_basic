import sys
sys.stdin = open("input.txt", 'r')


def dfs(pe):
    visited[pe] = 1
    for j in relation[pe]:
        if not visited[j]:
            dfs(j)


T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    relation = [[] for _ in range(N + 1)]
    for m in range(M):
        fst, snd = map(int, input().split())
        relation[fst].append(snd)
        relation[snd].append(fst)

    # 2
    # 7 3
    # 1 2
    # 5 7

    visited = [0] * (N + 1)

    cnt = 0
    for person in range(1, N + 1):
        if not visited[person]:
            dfs(person)
            cnt += 1

    print(f"#{t} {cnt}")