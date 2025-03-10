import sys
sys.stdin = open("input.txt", 'r')

TC = int(input())

for tc in range(1, TC + 1):
    N, T = map(int, input().split())
    cards = list(range(1, N + 1))
    cards_num = len(cards)
    ratio = int(cards_num * 0.63)

    for t in range(T):
        first_shuffle = cards[ratio + 1:] + cards[0: ratio + 1]
        middle = cards_num // 2 if cards_num % 2 == 0 else cards_num // 2 + 1
        first_cards = first_shuffle[: middle]
        second_cards = first_shuffle[middle:]

        if len(second_cards) < len(first_cards):
            second_cards += [0] * (len(first_cards) - len(second_cards))
        second_shuffle = []
        for i, j in zip(first_cards, second_cards):
            second_shuffle += [i, j]

        if second_shuffle[-1] == 0:
            cards = second_shuffle[:-1]
        else:
            cards = second_shuffle

    print(f"#{tc} {' '.join(map(str, cards))}")

