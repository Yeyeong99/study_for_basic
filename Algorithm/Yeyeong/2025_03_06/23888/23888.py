import sys

sys.stdin = open("input.txt", 'r')

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    nums_2 = ''.join([input().strip() for _ in range(N)])
    result = []
    for i in range(0, len(nums_2), 7):
        current = nums_2[i: i + 7][::-1]
        num_10 = 0
        for j in range(7):
            if current[j] == '1':
                num_10 += 2 ** j
        result.append(num_10)

    print(f"#{t} {' '.join(map(str, result))}")