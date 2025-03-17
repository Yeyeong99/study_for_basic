import sys
sys.stdin = open("input.txt", 'r')

relation = {}

T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())

    for m in range(M):
        fst, snd = map(int, input().split())
        relation[fst] = relation.get(fst, []) + [snd]
        relation[snd] = relation.get(snd, []) + [fst]

    print(relation)