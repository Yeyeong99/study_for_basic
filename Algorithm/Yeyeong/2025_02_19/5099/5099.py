import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    pizzas = list(map(int, input().split()))

    plates = [0] * N
    front = rear = 0

    i = 0
    index = [i for i in range(1, N + 1)]
    while True:
        plates[front] = plates[front] // 2

        if plates[front] == 0 and i < M:
            plates[front] = pizzas[i]
            index[front] = i + 1
            pizzas[i] = 0
            i += 1
        if plates == [0] * N:
            break
        current_plates = plates[:]
        front = (front + 1) % N

    for i in range(N):
        if current_plates[i] != 0:
            print(f"#{t} {index[i]}")

