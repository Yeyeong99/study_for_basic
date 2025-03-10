import sys
sys.stdin = open("input.txt", 'r')

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    cards = input().split()
    middle = N // 2 if N % 2 == 0 else N // 2 + 1
    first_cards = cards[: middle]
    second_cards = cards[middle:]

    if len(second_cards) < len(first_cards):
        second_cards += [0] * (len(first_cards) - len(second_cards))
    result = []
    for i, j in zip(first_cards, second_cards):
        result += [i, j]

    if result[-1] == 0:
        cards = result[:-1]
    else:
        cards = result

    print(f"#{t} {' '.join(cards)}")