import sys

sys.stdin = open("input.txt", "r")


def binary(nums):
    result = ''
    for n in nums:
        current = ''
        for j in range(4):
            current += str(n % 2)
            n //= 2
        result += current[::-1]
    return result


hex_dict = {
    'A': 10,
    'B': 11,
    'C': 12,
    'D': 13,
    'E': 14,
    'F': 15
}

T = int(input())

for t in range(1, T + 1):
    N, number = input().split()
    number = list(number)
    for i in range(len(number)):
        if number[i] in hex_dict.keys():
            number[i] = hex_dict[number[i]]
        else:
            number[i] = int(number[i])

    answer = binary(number)
    print(f"#{t} {answer}")

