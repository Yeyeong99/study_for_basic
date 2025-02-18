# for test_case in range(1, 10+1):
#
#     N = int(input())
#     floor = list(map(int, input().split()))
#
#     floor_diff = 0
#
#     for i in range(2, len(floor) - 2):
#         if floor[i] - floor[i-2] >= 2 and floor[i] - floor[i+2] >= 2 and \
#                 floor[i] - floor[i-1] >= 2 and floor[i] - floor[i+1] >= 2:
#
#             max_next = max(floor[i-2], floor[i-1], floor[i+1], floor[i+2])
#             floor_diff += (floor[i] - max_next)
#
#     print(f'#{test_case} {floor_diff}')

for test_case in range(1, 11):
    N = int(input())
    floor = list(map(int, input().split()))

    floor_diff = 0

    for i in range(2, N - 2):
        max_next = max(floor[i-2], floor[i-1], floor[i+1], floor[i+2])
        if floor[i] > max_next:
            floor_diff += floor[i] - max_next

    print(f'#{test_case} {floor_diff}')


