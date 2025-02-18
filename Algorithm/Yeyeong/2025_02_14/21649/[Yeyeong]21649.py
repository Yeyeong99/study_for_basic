import sys
sys.stdin = open("input.txt", "r")

T = 1

for t in range(1, T + 1):
    V, E = map(int, input().split())
    num_list = list(map(int, input().split()))
    num_dict = {}

    for num in num_list:
        num_dict.setdefault(num, [])

    for i in range(len(num_list) - 1):
        if i % 2 == 0:
            # 방향이 없으므로 양쪽 다 저장
            num_dict[num_list[i]].append(num_list[i + 1])
            num_dict[num_list[i + 1]].append(num_list[i])

    visited = [0] * 8
    result = []
    stack = [1]
    while len(stack) != 0:
        # 방문할 노드
        idx = stack.pop()

        # 가지 않은 노드라면 => 갔다고 저장
        if not visited[idx]:
            visited[idx] = 1
            result.append(idx)
        # 노드가 아직 이어져 있다면 => 스택에 거꾸로 추가 (이래야 순서 맞음)
        # 스택에 추가 되었으므로 빈 배열로 바꿔줌
        if len(num_dict[idx]) != 0:
            stack += num_dict[idx][::-1]
            num_dict[idx] = []

    print(f"#{t} {'-'.join(map(str, result))}")