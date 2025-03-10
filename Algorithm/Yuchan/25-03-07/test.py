



# print(bin(-5))
# print(bin(4))
# print(bin(~4))
# print(~4)
#
#
# print(bin(31))
#
# def to_binary_8bit(n):
#     return format(n, '08b')
#
# print(to_binary_8bit(31))

# print(0.1 + 0.1 + 0.1 == 0.3)

# print(1.8 * (10 ** 308))

'''
========================================================
SWEA 10726
========================================================
'''

# def solution():
#     target = M
#     for _ in range(N):
#         if target & 0x1 == 0:
#             return 'OFF'
#         target = target >> 1
#     return 'ON'
#
# T = int(input())
# for tc in range(1, T + 1):
#     N, M = map(int, input().split())
#     result = solution()
#     print(f'#{tc} {result}')

