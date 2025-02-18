
arr = list(input())

arr.insert(0, 'N')
N = len(arr)

switch = 0
for i in range(1, N):
    if arr[i] == 'Y':
        switch += 1
        arr[i] = 'N'
        for j in range(2, N):
            if i * j < N:
                if arr[i * j] == 'Y':
                    arr[i * j] = 'N'
                else:
                    arr[i * j] = 'Y'

print(switch)

#오후 4:39 완료
