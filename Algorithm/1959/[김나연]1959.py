```python
T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    N_list = list(map(int, input().split()))
    M_list = list(map(int, input().split()))
    
    sumList = []    

    if M >= N:
        gap = M - N
        for i in range(gap+1):
            currentSum = 0
            for j in range(N):
                currentSum += N_list[j] * M_list[j+i]
            sumList.append(currentSum)
    
    else:
        gap = N - M
        for i in range(gap+1):
            currentSum = 0
            for j in range(M):
                currentSum = N_list[j+i] * M_list[j]
            sumList.append(currentSum)

    maxSum = max(sumList)
    print(f'#{test_case} {maxSum}')
```
