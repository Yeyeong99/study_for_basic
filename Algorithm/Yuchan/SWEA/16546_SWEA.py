def baby_gin(arr):
    count_list = [0] * 10  # 0~9 숫자 개수 저장 리스트

    # 숫자 개수 세기
    for num in arr:
        count_list[num] += 1

    triplet_count = 0
    run_count = 0

    # Triplet 체크 (3개씩 같은 숫자가 있으면 제거)
    for i in range(10):
        if count_list[i] >= 3:
            triplet_count += count_list[i] // 3
            count_list[i] %= 3  # 3개씩 제거하고 남은 개수만 유지

    # Run 체크 (연속된 숫자 3개)
    for i in range(8):  # i+2까지 봐야 하므로 0~7까지 확인
        while count_list[i] >= 1 and count_list[i+1] >= 1 and count_list[i+2] >= 1:
            count_list[i] -= 1
            count_list[i+1] -= 1
            count_list[i+2] -= 1
            run_count += 1  # 한 번의 Run 발견

    # Triplet과 Run이 합쳐서 2개면 Baby Gin!
    return triplet_count + run_count == 2

# 입력 처리
T = int(input())
for test_case in range(1, T + 1):
    arr = list(map(int, input().strip()))  # 6자리 숫자 입력받아 리스트 변환

    # 결과 출력
    result = "true" if baby_gin(arr) else "false"
    print(f'#{test_case} {result}')
