import sys
sys.stdin = open("input.txt", 'r')


def hoare_partitioning(left, right):
    pivot = arr[left]

    i = left + 1
    j = right

    while i <= j:  # 교차가 될 때까지
        # i = 큰 값을 검색하면서 오른쪽으로 진행
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] >= pivot:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    # pivot 위치 확정 - swap이 되는 순간 j 위치가 pivot
    arr[left], arr[j] = arr[j], arr[left]
    return j


# left, right: 작업 범위
def quick_sort(left, right):
    if left < right:
        pivot = hoare_partitioning(left, right)
        quick_sort(left, pivot - 1)
        quick_sort(pivot + 1, right)


T = int(input())

for t in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    quick_sort(0, N - 1)
    print(f"#{t} {arr[N // 2]}")