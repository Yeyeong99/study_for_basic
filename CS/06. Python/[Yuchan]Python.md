# CS50 Lecture 6 - Python

> ### Meow

- Python에서 기본적인 함수 정의와 사용법을 설명
- 특정 횟수만큼 'Meow'를 출력하는 함수 예제
- 반복문(`for`, `while`)을 이용한 반복 실행 소개
- 함수 매개변수를 활용하여 출력 횟수를 조절하는 방법 설명

```py
# 'Meow'를 여러 번 출력하는 함수
def meow(n):
    for _ in range(n):
        print('Meow')

meow(3)  # 'Meow'를 세 번 출력
```

> ### Truncation

- Python에서 나눗셈 연산(`//`과 `/`)의 차이를 설명
- 정수 나눗셈(`//`)과 실수 나눗셈(`/`)의 차이
- `int()` 함수를 사용하여 소수점을 자르는(truncation) 방법 설명
- C에서는 정수 나눗셈을 할 경우 자동으로 버림 (`5 / 2 == 2` in C, `5 / 2 == 2.5` in Python)

- Python에서는 int 오버플로우 발생하지 않음<br/>
    -> 필요한 만큼 메모리를 동적으로 확장하여 값을 저장하기 때문

```py
print(10 / 3)  # 3.3333...
print(10 // 3)  # 3 (정수 나눗셈)
print(int(3.9))  # 3 (반올림이 아니라 버림)
```

> ### Exceptions

- Python에서 예외 처리를 다루는 `try`와 `except` 문법 소개
- `ValueError`, `ZeroDivisionError`와 같은 일반적인 예외 설명
- 예상치 못한 예외를 다룰 수 있도록 `except Exception as e` 활용

```py
try:
  x = int(input('Input : '))
except ValueError:
  print('Not integer')
else:
  print('Integer')
```

> ### Mario

- 중첩 반복문을 이용하여 피라미드 구조를 출력하는 방법 설명
- `range()` 함수와 문자열 조작 활용

```py
for i in range(4):
    print('?', end='')

print('?' * 4)
```
