import sys
sys.stdin = open("input.txt", 'r')


def check_run(card):
    card_pick = [0] * 10
    for c in range(len(card)):
        card_pick[card[c]] = 1

    for idx in range(len(card_pick) - 2):
        if card_pick[idx: idx + 3] == [1, 1, 1]:
            return True
    return False


def triplet(card):
    card_pick = [0] * 10
    for c in range(len(card)):
        card_pick[card[c]] += 1

    for idx in range(len(card_pick)):
        if card_pick[idx] >= 3:
            return True
    return False


T = int(input())

for t in range(1, T + 1):
    cards = list(map(int, input().split()))
    N = len(cards)

    winner = 0
    first, second = [], []
    for i in range(N):
        # 카드를 미리 나누고 비교하면 카드의 뽑는 순서가 반영되지 않음
        # 0 1 2 3 ... 12이어야 하는데
        # 0 1 2 .. 5 / 0 1 2 .. 5 이렇게 되어서 문제..

        if i % 2 == 1:
            first.append(cards[i])
            if len(first) >= 3 and (check_run(first) or triplet(first)):
                winner = 2
                break
        else:
            second.append(cards[i])
            if len(second) >= 3 and (check_run(second) or triplet(second)):
                winner = 1
                break

    print(f"#{t} {winner}")

