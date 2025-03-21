import sys
sys.stdin = open("input.txt", 'r')


def dfs(idx, total, way):
    global operators, max_total, min_total

    if idx == N - 1:
        min_total = min(min_total, total)
        max_total = max(max_total, total)
        return
    way.append(numbers[idx])
    for o in range(4):
        if operators[o] > 0:
            operators[o] -= 1
            if o == 0:
                current_total = total + numbers[idx + 1]
            elif o == 1:
                current_total = total - numbers[idx + 1]
            elif o == 2:
                current_total = total * numbers[idx + 1]
            elif o == 3:
                current_total = int(total / numbers[idx + 1])
            dfs(idx + 1, current_total, way + [o])
            operators[o] += 1
    way.pop()


T = int(input())

for t in range(1, T + 1):
    N = int(input())
    operators = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    max_total = -float("inf")
    min_total = float("inf")
    dfs(0, numbers[0], [])

    print(f"#{t} {max_total - min_total}")