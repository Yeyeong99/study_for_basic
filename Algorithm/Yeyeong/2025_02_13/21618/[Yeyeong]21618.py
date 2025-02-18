import sys
sys.stdin = open("input.txt", "r")

T = 1

for t in range(1, T + 1):
    V, E = map(int, input().split())
    num_list = list(map(int, input().split()))
    num_dict = {}

    # 그래프를 딕셔너리 형태로 저장
    for num in num_list:
        num_dict.setdefault(num, [])
    # 짝수 번째가 키값이 됨
    for i in range(len(num_list) - 1):
        if i % 2 == 0:
            num_dict[num_list[i]].append(num_list[i + 1])

    # 방문한 노드 저장
    visited = []
    # 인덱스 시작은 1
    index = [1]

    # 인덱스를 모두 사용할 때까지 반복
    while len(index) != 0:
        # 인덱스 배열에 들어있는 마지막 인덱스 꺼내기
        idx = index.pop()
        # 방문하지 않았으면 방문 배열에 저장
        if idx not in visited:
            visited.append(idx)
        # 현재 인덱스와 이어진 노드에 다른 노드가 이어져 있을 경우 인덱스에 추가하진 않음
        if [idx] in num_dict.values():
            continue
        # 현재 인덱스와 이어진 노드가 다른 노드와 이어져있지 않을 경우 다음 인덱스로 추가
        elif len(num_dict[idx]) != 0:
            # 방문 순서를 맞추려면 거꾸로 추가해야함
            index += num_dict[idx][::-1]
            num_dict[idx] = []

    print(f"#{t} {'-'.join(map(str, visited))}")
