import sys
sys.stdin = open("input.txt", "r")

numbers_str_to_int = {
    "ZRO": 0,
    "ONE": 1,
    "TWO": 2,
    "THR": 3,
    "FOR": 4,
    "FIV": 5,
    "SIX": 6,
    "SVN": 7,
    "EGT": 8,
    "NIN": 9
}

numbers_int_to_str = {}

for key, value in numbers_str_to_int.items():
    numbers_int_to_str[value] = key

T = int(input())

for t in range(1, T + 1):
    case, words_num = input().split()
    nums_str_input = input().spl0.it()

    # 문자열을 숫자로 변환
    nums_int = [numbers_str_to_int[num] for num in nums_str_input]
    nums_int.sort()  # 정렬

    # 숫자를 문자로 다시 변환
    nums_str = [numbers_int_to_str[num] for num in nums_int]

    print(f"#{t} {' '.join(nums_str)}")