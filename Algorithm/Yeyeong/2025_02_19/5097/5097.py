import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    # M번 만큼 반복해서 배열 생성
    result = [nums[i % N] for i in range(M)]

    # 해당 배열의 마지막에서 N 번째 숫자가 수열의 맨 앞에 있는 숫자
    print(f"#{t} {result[-N]}")

