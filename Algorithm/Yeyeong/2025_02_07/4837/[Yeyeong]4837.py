import sys
sys.stdin = open("input.txt", "r")

A = list(range(1, 13))
len_A = len(A)

T = int(input())
for t in range(T):
    N, K = map(int, input().split())
    count = 0
    for i in range(1 << len_A):
        sub_set = []
        for j in range(len_A):
            if i & (1 << j):
                sub_set.append((A[j]))

        if len(sub_set) == N and sum(sub_set) == K:
            count += 1

    print(count)
