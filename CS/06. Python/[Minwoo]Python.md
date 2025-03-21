### list

## 요약 : 파이썬은 메모리에 직접 관여 안 하니까 c처럼 배열 저장소 고민 하지말고 걍 쓰세요.

#### 1. **리스트(list)와 배열(array)의 차이**
   - Python의 리스트는 **자동 메모리 관리**가 되며, 크기가 동적으로 조정될 수 있음.
   - C 언어에서 배열(array)은 **연속된 메모리 공간**을 사용하지만, Python의 리스트는 **연결 리스트(linked list)**와 유사하게 동작함.
   - C에서 배열을 사용할 때는 포인터와 메모리 할당이 필요하지만, Python에서는 리스트를 단순히 사용할 수 있음.

#### 2. **리스트의 기본적인 활용**
   - 리스트는 **여러 값을 저장하는 데이터 타입**이며, `[]`(대괄호)를 사용해 생성.
   - 리스트의 **기본 메서드(methods)**: 
     - `.append(value)`: 리스트 끝에 값 추가
     - `sum(list)`: 리스트 내 모든 값을 더함
     - `len(list)`: 리스트의 길이(요소 개수) 반환

#### 3. **평균값 구하기 예제**
   ```python
   scores = [72, 73, 33]
   average = sum(scores) / len(scores)
   print(f"Average: {average}")
   ```
   - `sum()`과 `len()`을 활용해 리스트의 평균을 간단하게 계산 가능.

#### 4. **사용자로부터 입력 받아 리스트 생성**
   ```python
   from cs50 import get_int

   scores = []  # 빈 리스트 생성

   for i in range(3):
       score = get_int("Score: ")
       scores.append(score)  # 리스트에 추가

   average = sum(scores) / len(scores)
   print(f"Average: {average}")
   ```
   - `append()` 메서드를 사용하여 리스트에 값 추가.
   - C에서는 `malloc()`과 포인터를 사용해야 하지만, Python에서는 리스트가 자동으로 관리됨.

#### 5. **리스트를 활용한 검색 (Phonebook 예제)**
   - 사용자가 입력한 이름을 리스트에서 검색하는 방법:
   ```python
   names = ["Carter", "David", "John"]

   name = input("Name: ")    ## 이거 나만 몰랐나?

   if name in names:
       print("Found")
   else:
       print("Not found")
   ```
   - `if name in names:` 구문을 사용하여 리스트에서 값을 검색할 수 있음.
   - Python은 자동으로 **선형 탐색(linear search)**을 수행.

#### 6. **for-else 문 활용**
   ```python
   for n in names:
       if n == name:
           print("Found")
           break
   else:
       print("Not found")
   ```
   - `for` 루프 내에서 `break`가 실행되지 않으면 `else` 문이 실행됨.
   - 이는 특정 값을 찾지 못했을 때 실행되는 방식으로 활용 가능.

#### 7. **리스트 결합 방법**
   - 리스트를 `append()` 없이 `+` 연산자로 결합 가능:
   ```python
   scores = scores + [score]    # 형태는 꼭 str 더하는 것처럼 더하지만 새로운 리스트를 생성한다는 점에서 차이이
   ```
   - 하지만 기존 리스트를 수정하는 것이 아니라, **새로운 리스트를 생성**하는 방식이므로 `append()`가 더 효율적.

#### 8. **Python의 장점**
   - C보다 더 간결한 문법과 풍부한 내장 함수 제공.
   - `sum()`, `len()`, `append()` 등의 함수를 사용하여 직접 구현할 필요 없이 간단한 코드로 해결 가능.
   - `if name in names:`처럼 직관적인 표현 사용 가능.

---

### 결론
Python의 리스트는 C의 배열보다 **더 편리하게 사용할 수 있는 데이터 구조**로, **자동 메모리 관리, 동적 크기 조정, 다양한 내장 함수 지원** 등의 이점을 제공함. Python의 내장 기능을 활용하면 복잡한 작업을 간단하게 수행할 수 있으며, 검색, 추가, 평균 계산 등의 작업도 효율적으로 처리 가능.

### dictionary

## 역병규햄 피셜 : 나중에 배열에서 찾고 싶은 값을 찾아야할 때 배열이 커지면 메모리 터지니까 딕셔너리 쓰거라.

### 1. **딕셔너리 개념**
   - 딕셔너리는 키(key)와 값(value)으로 이루어진 데이터 구조로, C의 해시 테이블(hash table)과 유사합니다.
   - `{}` 중괄호를 사용하여 선언하며, `"key": "value"` 형태로 데이터를 저장합니다.
   - 예제:
     ```python
     phonebook = {
         "Carter": "+1-617-495-1000",
         "David": "+1-617-495-1000",
         "John": "+1-949-468-2750"
     }
     ```

### 2. **리스트와 딕셔너리를 함께 사용하는 방법**
   - 리스트의 각 요소를 딕셔너리로 저장할 수 있습니다.   # 나만 기억이 흐릿 한가요?
   - 예제:
     ```python
     people = [
         {"name": "Carter", "number": "+1-617-495-1000"},
         {"name": "David", "number": "+1-617-495-1000"},
         {"name": "John", "number": "+1-949-468-2750"}
     ]
     ```

### 3. **딕셔너리를 이용한 검색**
   - 기존 리스트를 순회하며 찾는 방식보다, 딕셔너리를 사용하면 더 빠르게 검색할 수 있습니다.
   - 기존 방식(리스트 순회):
     ```python
     name = input("Name: ")

     for person in people:            # 아니, 딕셔너리의 key값도 in 메서드로 가능했네요. 저만 몰랐어요?
         if person["name"] == name:
             print(f"Found {person['number']}")
             break
     else:
         print("Not found")
     ```
   - 개선된 방식(딕셔너리 사용):
     ```python
     name = input("Name: ")
     if name in phonebook:
         print(f"Found {phonebook[name]}")
     else:
         print("Not found")
     ```
   - 딕셔너리를 사용하면 `in` 연산자로 키를 빠르게 찾을 수 있어 더 효율적입니다.

### 4. **딕셔너리의 장점**
   - 리스트를 사용하면 특정 값을 찾기 위해 `O(n)` 시간이 걸리지만, 딕셔너리는 해시 테이블을 기반으로 하므로 평균 `O(1)`의 검색 속도를 가집니다.
   - 키-값 쌍을 자유롭게 추가할 수 있어 데이터 관리가 용이합니다.

### sys

## 우리가 맨날 텍스트 자동으로 읽어오게 하던 그 거 맞습니다. sys.stdin = open 어쩌구 저쩌구

# 복습  ㄱㄱ argv란?
1. sys.argv란?
sys.argv는 프로그램 실행 시 입력된 명령줄 인자들을 저장하는 리스트.
리스트의 첫 번째 요소(sys.argv[0])는 실행된 파일명
이후 요소(sys.argv[1], sys.argv[2]...)는 사용자가 입력한 인자들



![alt text](아저씨명강의.png)

이거 왜 헬로 월드가 아닌 아저씨가 입력한 이름이 나올까?

## 

1. **C와 Python의 차이점**  
   - C에서는 `main(argc, argv)`를 사용하지만, Python에서는 `sys.argv`를 통해 명령줄 인자를 가져온다.  
   - `sys.argv`는 리스트(`list`) 형태이며, 첫 번째 요소(`argv[0]`)는 실행된 스크립트 파일의 이름이다.

2. **명령줄 인자 처리**  
   - `len(sys.argv)`를 사용하여 인자의 개수를 확인할 수 있다.  
   - 특정 개수의 인자가 입력되지 않았을 경우 기본값을 설정하는 방식을 사용할 수 있다.


3. **프로그램 종료 (`sys.exit()`)**  
   - `sys.exit(0)`: 정상 종료  
   - `sys.exit(1)`: 오류 발생으로 종료  
   - C의 `return 0` 또는 `return 1`과 같은 역할을 한다.

4. **pip를 사용한 라이브러리 설치**  
   - Python에서는 외부 라이브러리를 쉽게 설치할 수 있으며, 예제로 `pip install face_recognition`을 보여줌.


#### pip(Package Installer for Python)    
Python 패키지(라이브러리)를 설치하고 관리하는 도구

### 1. **외부 라이브러리 설치 (`pip install`)**
   - `pip install cowsay`: ASCII 아트 기반의 대화형 소를 출력하는 라이브러리.
   - `pip install qrcode`: QR 코드를 생성할 수 있는 라이브러리.

   Python에서는 `pip`을 사용하여 간단하게 외부 라이브러리를 설치할 수 있음.

---

### 2. **ASCII 아트 출력 (`cowsay`)**
   ```python
   import cowsay
   
   name = input("What's your name? ")
   cowsay.cow(f"Hello, {name}")
   ```
   - `cowsay.cow("문자열")`을 사용하면 소가 해당 메시지를 출력함.
   - 다양한 캐릭터 (`cowsay.dragon()`, `cowsay.tux()`)를 사용할 수도 있음.

---
![alt text](아저씨이건좀.png)
### 3. **QR 코드 생성 (`qrcode`)**
   ```python
   import qrcode

   img = qrcode.make("https://www.youtube.com/watch?v=xvFZjo5PgG0")
   img.save("qr.png")
   ```
   - `qrcode.make(데이터)`를 사용하여 QR 코드 이미지 생성.
   - `img.save("파일명.png")`으로 QR 코드 이미지를 저장 가능.

---

## never gonna give you up  짱 명곡이니 복습하며 들어보세요요

### 4. **Python의 강점**
   - C에서는 직접 메모리 관리 및 복잡한 작업이 필요하지만, Python에서는 간단한 코드로 같은 기능을 구현 가능.
   - 라이브러리를 활용하면 ASCII 아트, QR 코드 생성 등 다양한 작업을 쉽게 수행할 수 있음.

