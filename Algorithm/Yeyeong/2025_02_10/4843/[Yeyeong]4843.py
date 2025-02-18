import sys
sys.stdin = open("input.txt", "r")

# 오름차순으로 정렬
# 내림차순으로 정렬
# 두 가지를 합침


def selection_sort_asc(arr, N):
    a = arr[:]
    for i in range(N - 1):
        min_idx = i
        for j in range(i + 1, N):
            if a[min_idx] > a[j]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a


def selection_sort_desc(arr, N):
    a = arr[:]
    for i in range(N - 1):
        max_idx = i
        for j in range(i + 1, N):
            if a[max_idx] < a[j]:
                max_idx = j
        a[i], a[max_idx] = a[max_idx], a[i]
    return a


T = int(input())

for t in range(1, T + 1):
    N = int(input())
    num_list = list(map(int, input().split()))

    # 답을 리턴하기 위한 길이 10인 리스트 선언
    result = [0 for i in range(10)]

    desc = selection_sort_desc(num_list, N)
    asc = selection_sort_asc(num_list, N)

    # 인덱스가 짝수 일 때 => 내림차순에서
    # desc의 인덱스: 0 1 2 3 4
    # result의 인덱스: 0 2 4 6 8
    # 인덱스가 홀수 일 때 => 오름차순에서
    # asc의 인덱스: 0 1 2 3 4
    # result의 인덱스: 1 3 5 7 9
    for i in range(10):
        if i % 2 == 0:
            result[i] = desc[i // 2]
        else:
            result[i] = asc[(i - 1) // 2]

    print(f"#{t} {' '.join(map(str, result))}")