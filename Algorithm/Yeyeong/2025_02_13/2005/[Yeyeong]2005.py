import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for t in range(1, T + 1):
    N = int(input())

    triangle = [[1]]

    print(f"#{t}")
    # triangle의 마지막에 들어오는 값으로 stack을 업데이트
    for n in range(N):
        stack = triangle[-1]
        print(' '.join(map(str, stack)))

        # 다음 줄 만들기
        # 첫 번째, 마지막은 항상 1
        num_line = [1]
        for s in range(len(stack) - 1):
            # 전 줄의 마지막 값을 없애줌(pop)
            # pop한 값과 전 줄의 새로운 마지막 값을 더함
            # 그 값을 num_line에 추가
            num = stack.pop() + stack[-1]
            num_line.append(num)
        # 마지막 값
        num_line.append(1)
        triangle.append(num_line)


