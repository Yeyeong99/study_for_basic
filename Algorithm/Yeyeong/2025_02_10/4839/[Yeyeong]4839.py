import sys
sys.stdin = open("input.txt", "r")

# 재귀가 몇 번 수행되었는지를 알기 위해 count라는 변수도 추가


def binary_search(start, end, key, count):
    middle = (start + end) // 2
    count += 1
    if middle == key:
        return count
    elif middle < key:
        return binary_search(middle + 1, end, key, count)
    else:
        return binary_search(start, middle - 1, key, count)


T = int(input())

for t in range(1, T + 1):
    P, A, B = map(int, input().split())

    a = binary_search(1, P, A, 0)
    b = binary_search(1, P, B, 0)

    result = ''
    if a < b:
        result = 'A'
    elif a == b:
        result = 0
    else:
        result = 'B'

    print(f"#{t} {result}")
