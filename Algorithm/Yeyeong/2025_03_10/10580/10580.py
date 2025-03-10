import sys
sys.stdin = open("input.txt", 'r')

TC = int(input())

for tc in range(1, TC + 1):
    N = int(input())
    heights = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0
    for i in range(N):
        for j in range(i + 1, N):
            current = heights[i]
            next_height = heights[j]
            if current[0] < next_height[0] and current[1] > next_height[1]:
                cnt += 1
            elif current[0] > next_height[0] and current[1] < next_height[1]:
                cnt += 1

    print(f"#{tc} {cnt}")