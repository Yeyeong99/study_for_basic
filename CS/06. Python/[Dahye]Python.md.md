# CS50_[이다혜] Python

작성 일시: 2025년 3월 19일 오후 4:21

## Python

---

### 🍎 hello, world! 프린트 하기- C VS Python

### 1. **C 언어에서 "Hello, World!" 출력**

```c

#include <stdio.h>

int main() {
    printf("Hello, World!\n");
    return 0;
}

```

### **특징 및 과정**

- `#include <stdio.h>`: 표준 입출력 라이브러리 `stdio.h`를 포함해야 `printf` 함수를 사용할 수 있음.
- `int main() {}`: C 프로그램의 진입점(`main` 함수)을 명확히 정의해야 함.
- `printf("Hello, World!\n");`: 화면에 문자열을 출력하는 함수. `\n`은 줄바꿈 문자.
- `return 0;`: 프로그램이 정상적으로 종료되었음을 운영체제에 알림.

---

### 2. **Python에서 "Hello, World!" 출력**

```python

print("Hello, World!")

```

### **특징 및 과정**

- `print()` 함수만으로 출력이 가능함.
- `#include`나 `main()` 함수 같은 것이 필요 없음.
- 코드가 간결하고 가독성이 높음.

### 

---

### **🍎 컴파일러 vs 인터프리터**

프로그래밍 언어로 작성한 코드는 컴퓨터가 직접 이해할 수 없기 때문에 기계어(바이너리 코드)로 변환하는 과정이 필요. 이때 변환 방식에 따라 컴파일러와 인터프리터로 나뉨. 

**컴파일러(Compiler)**

- 한 번에 전체 코드를 기계어로 변환한 후 실행하는 방식

**인터프리터(Interpreter)**

- 코드를 한 줄씩 해석하면서 실행하는 방식

### **🍎컴파일러 vs 인터프리터 비교**

|  | **컴파일러** | **인터프리터** |
| --- | --- | --- |
| 실행 방식 | 전체 코드를 한 번에 변환 후 실행 | 한 줄씩 읽고 즉시 실행 |
| 실행 속도 | 빠름 (미리 변환 완료) | 느림 (실행 시마다 변환) |
| 오류 처리 | 컴파일할 때 한 번에 확인 | 실행하면서 오류가 나면 중단 |
| 배포 | 실행 파일만 배포 가능 | 소스 코드와 인터프리터 필요 |
| 대표 언어 | C, C++, Rust, Java | Python, JavaScript, PHP |

### **🍎C vs Python 라이브러리 사용 방식 비교**

|  | **C 언어** | **Python** |
| --- | --- | --- |
| **표준 라이브러리** | `#include <library.h>` 사용 | `import library` 사용 |
| **외부 라이브러리 설치** | 직접 다운로드 & 빌드 필요 | `pip install`로 간단히 설치 |
| **사용 방식** | 헤더 포함 & 컴파일 필요 | 인터프리터에서 바로 실행 가능 |
| **배포 방식** | 바이너리 파일 포함 필요 | `requirements.txt` 등으로 쉽게 공유 가능 |
| **호환성** | 플랫폼 의존적 (컴파일 필요) | 플랫폼 독립적 (Python이 설치되어 있으면 실행 가능) |

---

요약: 

- **C 언어**는 **라이브러리를 직접 다운로드하고 컴파일 과정이 필요**하지만, **최적화가 잘 되어 성능이 뛰어남**
- **Python**은 **라이브러리를 쉽게 설치하고 사용할 수 있어 개발 속도가 빠름**, 하지만 **성능은 C보다 다소 떨어질 수 있음**

### **🍎C 언어 vs Python 비교 요약**

| 구분 | **C 언어** | **Python** |
| --- | --- | --- |
| **언어 유형** | 저수준 언어 (하드웨어 가까움) | 고수준 언어 (사용자 친화적) |
| **컴파일 vs 인터프리터** | 컴파일 언어 (소스 → 기계어 변환 후 실행) | 인터프리터 언어 (한 줄씩 해석하며 실행) |
| **실행 속도** | 빠름 (기계어로 변환됨) | 느림 (인터프리터 실행 방식) |
| **메모리 관리** | 개발자가 직접 관리 (동적 메모리 할당 & 해제) | 자동 관리 (가비지 컬렉터) |
| **문법** | 엄격 (자료형 명시, 세미콜론 `;` 필수) | 유연함 (동적 타이핑, 세미콜론 불필요) |
| **라이브러리 관리** | 직접 다운로드 & 빌드 필요 | `pip`로 간편 설치 가능 |
| **배포 방식** | 실행 파일(`.exe` 등) 생성 후 배포 | 소스 코드 & 인터프리터 필요 |
| **포인터 사용** | 가능 (메모리 직접 제어 가능) | 불가능 (안전성 높음) |
| **사용 목적** | 시스템 프로그래밍, 임베디드, 게임 엔진 | 데이터 분석, 웹 개발, AI/ML, 자동화 |
| **대표적인 활용 예시** | 운영체제, 드라이버, 게임 엔진 (Unreal) | 웹 개발(Django), 데이터 과학, 인공지능 |

---

- **C 언어**: 성능 최적화 & 하드웨어 제어가 필요한 경우
- **Python**: 빠른 개발 & 쉬운 유지보수가 필요한 경우

## Speller

---

- **문장의 철자(spelling)를 검사하고 교정하는 프로그램 또는 기능**
- **Python의 `pyspellchecker` 라이브러리**를 이용해 철자 검사 가능

```python

from spellchecker import SpellChecker

spell = SpellChecker()
word = "pyhton"  # 오타 포함
corrected = spell.correction(word)

print(f"'{word}'의 올바른 철자는 '{corrected}'입니다.")
# 출력: 'pyhton'의 올바른 철자는 'python'입니다.

```

### **Speller가 활용되는 분야**

✅ 문서 작성 소프트웨어 (MS Word, Google Docs)

✅ 웹 브라우저 (Chrome, Firefox)

✅ 검색 엔진 (Google, Bing)

✅ 모바일 키보드 자동 수정 기능

✅ 프로그래밍 언어(텍스트 데이터 처리, NLP 분야)

---

네 가지 기능을 구현해 보겠다고 함. 

check()함수, load()함수, size()함수, unload()함수

```python
words = set()

def check(word):
    return word.lower() in words

def load(dictionary):
    with open(dictionary) as file:
        words.update(file.read().splitlines())
    return True

def size():
    return len(words)

def unload():
    return True
```

파이썬에선  malloc() free() pointer() 등이 필요없고 간편하고 좋은데 왜 모두들 파이썬을 쓰진 않을까? 청중에게 질문 던짐.

→ 파이썬이 c보다 느리고 더 많은 ram 메모리를 차지함. 

## **🍎Python이 C보다 느린 이유**

**주로 실행 방식과 메모리 관리 차이 때문**

| **이유** | **C 언어** | **Python** |
| --- | --- | --- |
| **실행 방식** | 컴파일 언어 → 기계어로 변환 후 실행 | 인터프리터 언어 → 한 줄씩 해석하며 실행 |
| **타입 체크** | 정적 타이핑 (컴파일 시 타입 결정) | 동적 타이핑 (실행 중 타입 체크) |
| **메모리 관리** | 직접 관리 (malloc/free) | 가비지 컬렉터 자동 관리 |
| **추상화 수준** | 저수준 (하드웨어와 가까움) | 고수준 (추상화가 많음) |

**C는 미리 컴파일**되어 기계어로 실행 → 빠름

**Python은 실행 중에 해석**하면서 실행 → 느림

**Python은 동적 타이핑**이라 실행 도중 타입 체크 필요 → 추가 오버헤드 발생

**결론:** Python은 **실행할 때마다 변환하고 타입을 체크하기 때문에 C보다 느림**

---

## **🍎Python이 C보다 메모리를 더 많이 차지하는 이유**

**자동 메모리 관리**와 **객체 기반 설계** 때문

| **이유** | **C 언어** | **Python** |
| --- | --- | --- |
| **데이터 저장 방식** | 기본 데이터 타입 (int, float 등) | 모든 것이 객체(Object) |
| **메모리 관리** | 수동 할당 & 해제 (`malloc/free`) | 자동 관리 (가비지 컬렉션) |
| **추가적인 오버헤드** | 최소한의 데이터 크기 유지 | 포인터, 레퍼런스 카운팅 등 추가 정보 저장 |
1. **모든 것이 객체** → `int`, `float` 같은 기본 타입도 객체라서 추가 메모리 사용
2. **가비지 컬렉션 사용** → 불필요한 객체를 자동으로 제거하지만, 추가적인 메모리 오버헤드 발생
3. **동적 타입 시스템** → 변수 타입을 저장하고 관리해야 하므로 메모리 사용 증가

**결론:** Python은 **편리한 기능을 제공하는 대신 메모리를 더 많이 차지함**

## **🍎Python의 속도를 개선하는 방법**

 **1. C 확장 사용 (`Cython`, `NumPy`)**

- Python의 느린 부분을 C로 구현
- 예: `NumPy`는 내부적으로 C로 구현되어 빠름

 **2. JIT 컴파일 (`PyPy`)**

- pypy를 사용하면 실행 속도가 5~10배 빨라질 수 있음!

**3. 멀티스레딩 & 병렬 처리**

- `multiprocessing`을 활용해 여러 CPU를 동시에 사용하면 성능 향상 가능

**4. C와 함께 사용 (`C extension`, `C API`)**

- 성능이 중요한 부분은 C로 구현하고, 나머지는 Python으로 개발하는 하이브리드 방식 사용

## Filter

---

사진에 블러 효과 적용하는 법

`image.filter(ImageFilter.BLUR)` 

```python

from PIL import Image, ImageFilter

# 이미지 열기
image = Image.open("example.jpg")

# 블러 필터 적용
blurred_image = image.filter(ImageFilter.BLUR)

# 블러 처리된 이미지 저장 & 보기
blurred_image.save("blurred_example.jpg")
blurred_image.show()

```

Pillow(`PIL`) 라이브러리에서 다양한 블러 효과를 쉽게 적용 가능

- **`ImageFilter.BLUR`** → 기본적인 블러
- **`ImageFilter.GaussianBlur(radius=n)`** → 더 강한 블러

## Face recognition

## 1. **얼굴 인식** 라이브러리**`face_recognition`**

---

- **Dlib의 딥러닝 모델**을 사용하여 얼굴을 감지하고 인식
- 얼굴 **탐지(Detection)**, **특징점 추출(Landmarks)**, **얼굴 비교(Recognition)** 가능
- **빠르고 정확**하며, Python 코드 몇 줄로 얼굴 인식을 구현할 수 있음

---

## **2. 설치 방법 (`face_recognition` & `dlib`)**

✅ **Windows에서 설치**

```

pip install face_recognition
pip install opencv-python

```

✅ **Mac/Linux에서 설치**

```

brew install cmake dlib
pip install face_recognition
pip install opencv-python

```

- `opencv-python`도 함께 설치하면 **이미지 & 비디오 처리**에 활용 가능!

---

## **3. 얼굴 인식 기능 예제**

### **(1) 얼굴 감지 (탐지)**

```python

import face_recognition
import cv2

# 이미지 로드
image = face_recognition.load_image_file("people.jpg")

# 얼굴 위치(좌표) 찾기
face_locations = face_recognition.face_locations(image)

print(f"이미지에서 {len(face_locations)}개의 얼굴을 찾았습니다.")

# 얼굴 위치 출력 (좌표값: (top, right, bottom, left))
for face in face_locations:
    print(face)

```

👉 `face_recognition.face_locations()`을 사용하면 이미지에서 얼굴 위치(좌표)를 찾아줌.

---

### **(2) 얼굴 특징점 찾기 (눈, 코, 입 등)**

```python
python
복사편집
import face_recognition
import cv2

# 이미지 로드
image = face_recognition.load_image_file("face.jpg")

# 얼굴 특징점(landmarks) 찾기
face_landmarks_list = face_recognition.face_landmarks(image)

print("얼굴 특징점:", face_landmarks_list)

```

📌 **`face_recognition.face_landmarks()`**를 사용하면 눈, 코, 입 등의 위치를 찾을 수 있어!

---

### **(3) 얼굴 비교 (얼굴 인식)**

```python
python
복사편집
import face_recognition

# 기준 얼굴 이미지 로드
known_image = face_recognition.load_image_file("known.jpg")
known_encoding = face_recognition.face_encodings(known_image)[0]

# 비교할 얼굴 이미지 로드
unknown_image = face_recognition.load_image_file("unknown.jpg")
unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

# 얼굴 비교 (True/False 반환)
results = face_recognition.compare_faces([known_encoding], unknown_encoding)

if results[0]:
    print("두 얼굴이 일치합니다!")
else:
    print("얼굴이 다릅니다.")

```

👉 **`face_recognition.compare_faces()`**를 사용하면 얼굴이 같은지 비교할 수 있어!

---

### **(4) 실시간 얼굴 인식 (웹캠 활용)**

```python

import cv2
import face_recognition

# 웹캠 켜기
video_capture = cv2.VideoCapture(0)

while True:
    # 프레임 읽기
    ret, frame = video_capture.read()

    # 얼굴 위치 찾기
    face_locations = face_recognition.face_locations(frame)

    # 얼굴 주위에 사각형 그리기
    for (top, right, bottom, left) in face_locations:
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

    # 화면에 표시
    cv2.imshow('Face Recognition', frame)

    # 'q' 키를 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 웹캠 종료
video_capture.release()
cv2.destroyAllWindows()

```

👉 **웹캠에서 얼굴을 감지하고 실시간으로 표시**