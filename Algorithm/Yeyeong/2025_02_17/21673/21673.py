T = int(input())

for t in (1, T + 1):
    numbers = list(input())

    for i in range(len(numbers) - 1):
        if numbers[i] == '*' or numbers[i] == '/':
            numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
