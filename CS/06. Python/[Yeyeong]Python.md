# Compare

## int

```python
from cs50 import get_int

x = get_int("x: ")
y = get_int("y: ")

if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y")

```

- 예상과 같이 결과가 나옴

## str

```python
s = input("s: ")
t = input("t: ")
if s == t:
    print("same")
else:
    print("different")
```

- 파이썬에서는 값이 같으면 same이 출력되고 다르면 different가 출력되지만, C는 같은 형식의 코드를 실행했을 때 항상 different가 나옴
- C에서는 string이 char\*와 같음. 주소값을 비교하기 때문에 같은 값을 입력하더라도 다른 변수라면 다르다고 인식함

### agree.py

```python
s = input("Do you agree? ")

if s == "Y" or s == "y":
    print("Agreed")
elif s == "N" or s == "n":
    print("Disagreed")
```

- 입력값이 Y, y, N, n 중 없다면 출력되는 결과값은 없음.

```python
if s in ["y", "yes", "Y", "YES", "Yes"]:
    print("Agreed")
elif s in ["n", "no", "N", "NO", "No"]:
    print("Not Agreed")
```

- 이런 식으로 모든 경우를 생각해 in을 사용하여 예상되는 예외 상황을 대처할 수 있음
- 하지만 이게 최선일까?
  - upper(), lower() 과 같은 메소드를 사용해 답변을 통일할 수 있을 거임

# OOP

- 객체 지향 프로그래밍: 파이썬의 모든 데이터 타입은 객체(각 객체는 특정 클래스에 속함), 메소드를 포함
- 메소드: 객체에 내장되어 있는 함수
  - 객체의 데이터를 조작하거나 특정 동작을 수행하는 데 사용됨

| 객체                                                                                                    | 클래스                                                                            |
| :------------------------------------------------------------------------------------------------------ | :-------------------------------------------------------------------------------- |
| 데이터와 그 데이터를 조작하는 함수(메소드)를 포함하는 개념적 단위. 파이썬의 모든 데이터는 객체로 표현됨 | 객체를 생성하기 위한 설계도나 템플릿, 객체의 속성(데이터)과 행동(메소드)을 정의함 |

## 절차지향과 객체지향

절차 지향 프로그래밍과 객체 지향 프로그래밍은 두 가지 주요한 프로그래밍 패러다임

| **특징**            | **절차 지향 프로그래밍**                                                   | **객체 지향 프로그래밍**                                                             |
| ------------------- | -------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| **중점**            | 함수(절차) 중심                                                            | 객체와 클래스 중심                                                                   |
| **데이터 및 함수**  | [데이터와 함수는 별개로 존재](#절차-지향-프로그래밍procedural-programming) | [데이터와 함수가 객체 내에 통합됨](#객체-지향-프로그래밍object-oriented-programming) |
| **프로그램 구조**   | 함수의 순차적 호출                                                         | 객체 간의 상호작용                                                                   |
| **데이터 접근**     | 데이터가 자유롭게 이동                                                     | 데이터가 객체 내에서 제어됨                                                          |
| **코드 재사용성**   | 낮음                                                                       | 높음 (상속, 다형성)                                                                  |
| **보안성**          | 낮음 (데이터 노출 위험)                                                    | 높음 (데이터 캡슐화)                                                                 |
| **적합한 프로젝트** | 작은 규모, 단순한 작업                                                     | 복잡한 시스템, 유지보수 필요                                                         |

### **절차 지향 프로그래밍(Procedural Programming)**

- 프로그램을 일련의 절차나 함수로 나누어 순차적으로 실행하는 방식
- 데이터와 함수는 별개로 존재하며, 함수가 데이터를 조작
- 작은 규모의 프로그램이나 단순한 작업에 적합.

```python
# 절차 지향 프로그래밍 예시
def calculate_area(length, width):
    return length * width

# 데이터
length = 5
width = 10

# 함수 호출
area = calculate_area(length, width)
print(f"Area: {area}")
```

### **객체 지향 프로그래밍(Object-Oriented Programming)**

- 프로그램을 객체와 클래스로 나누어, 객체가 데이터와 그 데이터를 조작하는 함수(메소드)를 포함하는 방식
- 복잡한 시스템을 모델링하고 코드의 재사용성을 높이는 데 유리함

```python
# 객체 지향 프로그래밍 예시
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

# 객체 생성
rect = Rectangle(5, 10)

# 메소드 호출
area = rect.calculate_area()
print(f"Area: {area}")
```

## agree.py의 개선

```python
s = input().lower()

if s in ["y", "yes"]:
    print("Agreed")

elif s in ["n", "no"]:
    print("Not Agreed")
```

- agree.py의 경우 string의 lower 메소드로 답변을 통일시켜 예외 상황을 처리함

# loop

```python
for i in range(3):
    print("I want to go home")
```

- python for iteration의 특징: i ++ 와 같이 명시하지 않아도 알아서 i 값을 증가시킴
- iterable하면 무엇이든 쉽게 loop 돌릴 수 있음

## uppercase.py

```python
before = input("Before: ")
print("After: ")
for c in before:
    print(c.upper())
```

```python
# 결과
Before: cat
After:
C
A
T
```

```python
before = input("Before: ")
print("After: ", end="")
for c in before:
    print(c.upper(), end="")
print()
```

```python
# 결과
Before: cat
After: CAT
```

- end: named parameter, 줄바꿈을 바꿔준다. default는 \n
  - 이전까지는 parameter의 순서를 사용했지만 end와 같이 이름을 직접 명시해 지정해줄 수도 있음

```python
before = input("Before: ")
print("After: ", end="")
print(before.upper())
```

```python
before = input("Before: ")
after = before.upper()
print(f"After: {after}")
```

```python
before = input("Before: ")
print(f"After: {before.upper()}")
```

```python
# 결과
Before: cat
After: CAT
```
