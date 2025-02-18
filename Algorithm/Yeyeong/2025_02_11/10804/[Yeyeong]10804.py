import sys
sys.stdin = open("input.txt", "r")

words = {
    'b': 'd',
    'd': 'b',
    'p': 'q',
    'q': 'p'
}

T = int(input())

for t in range(1, T + 1):
    word = input()
    print(f"#{t} {''.join([words[w] for w in word][::-1])}")
