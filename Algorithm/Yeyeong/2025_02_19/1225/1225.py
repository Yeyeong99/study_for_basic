import sys
sys.stdin = open("input.txt", "r")

T = 10

for t in range(1, T + 1):
    tc = int(input())
    nums = list(map(int, input().split()))

    i = 0  # nums의 각 숫자를 가리킬 인덱스
    reduce = 1  # 얼마나 감소시킬지
    while nums[-1] != 0:
        if reduce != 0:
            nums[i] -= reduce
            if nums[i] < 0:
                nums = nums[i + 1:] + [0]
                break
            else:
                nums = nums[i + 1:] + [nums[i]]
        reduce = (reduce + 1) % 6
    print(f"#{tc} {' '.join(map(str, nums))}")
