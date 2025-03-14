import sys
sys.stdin = open("input.txt", 'r')

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    carrots = list(map(int, input().split()))
    carrots.sort()
    freq = {}
    for c in carrots:
        freq[c] = freq.get(c, 0) + 1

    max_cap = N // 2

    # 조건 4: 한 상자에 N//2개 초과 금지
    if any(v > max_cap for v in freq.values()):
        print(f"#{t} -1")
        continue

    sizes = sorted(freq.keys())
    min_diff = float('inf')

    # 가능한 모든 3분할 조합 생성
    for i in range(1, len(sizes)):
        for j in range(i + 1, len(sizes)):
            box1 = sum(freq[s] for s in sizes[:i])
            box2 = sum(freq[s] for s in sizes[i:j])
            box3 = sum(freq[s] for s in sizes[j:])

            if box1 == 0 or box2 == 0 or box3 == 0:
                continue
            if max(box1, box2, box3) > max_cap:
                continue

            diff = max(box1, box2, box3) - min(box1, box2, box3)
            min_diff = min(min_diff, diff)

    print(f"#{t} {min_diff if min_diff != float('inf') else -1}")


