T = int(input())
# 여러 개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    if n == m:
        result = sum([i * j for i, j in zip(a, b)])
    else:
        if len(a) == min(n, m):
            min_list, max_list = a, b
        else:
            min_list, max_list = b, a

        zeros = max(n, m) * [0]
        lists = []

        for i in range(abs(n - m) + 1):
            for j in range(i, len(max_list)):
                try:
                    zeros[j] = min_list[j - i]
                except:
                    continue
            lists.append(zeros)

            zeros = max(n, m) * [0]

        sum_mul = 0
        answer = []
        for num in lists:
            for i, j in zip(num, max_list):
                mul = i * j
                sum_mul += mul
            answer.append(sum_mul)
            sum_mul = 0
        
        print(f'#{test_case} {max(answer)}')