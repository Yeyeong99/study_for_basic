arr = list(input())

result = 0
number = len(arr)

if set(arr) == {'N'}:
    print(0)
else:
    for n in range(1, number + 1):
        if arr[n - 1] == 'Y':
            for i in range(n, number + 1):
                if i % n == 0 and arr[i - 1] == 'Y':
                    arr[i - 1] = 'N'
                elif i % n == 0 and arr[i - 1] == 'N':
                    arr[i - 1] = 'Y'
        else:
            continue

        result += 1
        if set(arr) == {'N'}:
            print(result)
            break

    if set(arr) != {'N'}:
        print(-1)
