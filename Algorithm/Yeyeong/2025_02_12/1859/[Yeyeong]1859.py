import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    prices = list(map(int, input().split()))

    max_price = -float('inf')
    profit = 0

    for i in range(N - 1, -1, -1):
        if prices[i] < max_price:
            profit += max_price - prices[i]
        else:
            max_price = prices[i]
    print(f"#{t} {profit}")
