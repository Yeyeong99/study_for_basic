import sys
sys.stdin = open("input.txt", 'r')


def merge(left, right):
    global cnt
    result = [0] * (len(left) + len(right))
    l = r = 0

    # 비교 대상이 남아있을 때까지 반복
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result[l + r] = left[l]
            l += 1
        else:
            result[l + r] = right[r]
            r += 1

    # while 문이 끝나고
    # 왼쪽 리스트에 남은 데이터들을 모두 result 에 추가
    while l < len(left):
        result[l + r] = left[l]
        l += 1
    # 오른쪽 리스트에 남은 데이터들을 모두 result 에 추가
    while r < len(right):
        result[r + l] = right[r]
        r += 1

    return result


def merge_sort(li):
    global cnt
    if len(li) == 1:
        return li

    # 절반씩 분할
    mid = len(li) // 2
    left = li[:mid]  # 앞쪽 절반
    right = li[mid:]  # 뒤쪽 절반

    left_list = merge_sort(left)
    right_list = merge_sort(right)
    if left_list[-1] > right_list[-1]:
        cnt += 1
    # 분할이 완료되면 병합
    merged_list = merge(left_list, right_list)
    return merged_list


T = int(input())

for t in range(1, T + 1):
    N = int(input())
    cnt = 0
    nums = list(map(int, input().split()))
    merged_nums = merge_sort(nums)
    print(f"#{t} {merged_nums[N // 2]} {cnt}")