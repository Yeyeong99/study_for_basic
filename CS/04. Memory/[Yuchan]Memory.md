# CS50 Lecture 4 - Memory

> ###  Garbage Values 

- 변수를 선언했지만 초기화하지 않으면 이전 메모리 값(쓰레기 값, Garbage Value)이 남아있음
- C에서 변수를 선언할 때, 메모리에서 할당된 위치에는 기존 데이터가 남아있을 가능성이 있음
- 해결 방법 :
  - 변수를 명시적으로 초기화한다 (`int x = 0;`)
  - 동적 메모리 할당 후 `malloc()`이 반환한 포인터를 `NULL` 체크 후 사용
    * `malloc()` : memory allocation의 줄임말, C에서 동적 메모리 할당을 위해 사용하는 함수
> ### Pointer Fun with Blinky 

- 포인터는 메모리 주소를 저장하는 변수로, `*`를 사용하여 값을 참조
- `int *p`는 `p`가 정수를 가리키는 포인터임을 의미
- 예제 코드 분석:
  ```c
  int main(void)
  {
      int *x;
      int *y'  // int의 주소를 저장할 변수 x, y
  
      x = malloc(sizeof(int));  // pointer x, pointee malloc
                                
      *x = 42;  // 역참조 연산자 * : malloc에서 얻은 주소로 가서 값을 저장해라
      *y = 13;  // y에게 아직 value를 주지 않음(malloc하지 않음)
                // 따라서 y에는 garbage value가 있을것이다
  
      y = x;  // 그러니 x를 y에 복사하여 유요한 값을 부여하고
      
      *y = 13;  // 할당하자
  }
  ```
- 올바른 메모리 접근을 위해 포인터 사용 시 주의 필요

> ### Swapping

- 두 변수의 값을 교환하는 기본적인 방법과 포인터를 활용한 방법을 소개
- 잘못된 스왑 예제 (Call by Value):
  ```c
  void swap(int a, int b) 
  {
      int temp = a;
      a = b;
      b = temp;
  }
  ```
  `a`와 `b`가 복사본이기 때문에 원본 값이 변경되지 않음<br/>

- 올바른 스왑 예제 (Call by Reference):
  ```c
  void swap(int *a, int *b) 
  {
      int temp = *a;
      *a = *b;
      *b = temp;
  }
  ```
  포인터를 사용하여 원래 변수의 값을 직접 변경할 수 있음

![image](https://raw.githubusercontent.com/Y00CHAN/Images/refs/heads/master/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202025-03-13%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%209.10.40.png)
![image](https://raw.githubusercontent.com/Y00CHAN/Images/refs/heads/master/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202025-03-13%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%209.32.47.png)


> ### Overflow

- 데이터 타입의 크기를 초과하는 연산이 발생할 경우 오버플로우(Overflow)가 발생
- array, heap, stack 모두 buffer -> 함수 호출, 유튜브 몇 초 미리 다운로드, 인쇄 대기 등 -> 넘치면? Overflow
- 보안 소프트웨어 업체 CrowdStrike -> 오버플로우로 백억 단위 손해
- 예제 : `char`는 -128 ~ 127 범위를 가짐
  ```c
  char c = 127;
  c = c + 1;  // Overflow 발생, c 값은 -128이 됨
  ```
- 오버플로우 방지를 위해 :
  - 데이터 타입의 범위를 고려하여 프로그래밍
  - `unsigned`와 `signed` 타입 차이를 이해하고 사용
  - 더 큰 데이터 타입(`long`, `long long`) 활용

> ### in Python...

- 파이썬은 기본적으로 메모리 관리를 자동으로 수행
- C처럼 직접 메모리 주소를 조작하는 기능은 제공하지 않음
  - 하지만 아래와 같은 방법이 있음 
    ```py
    import ctypes

    a = ctypes.c_int(10)  # C의 int 타입을 생성
    ptr = ctypes.pointer(a)  # 포인터 생성

    print(ptr.contents)  # 10
    ptr.contents.value = 20  # 포인터를 통해 값 변경
    print(a.value)  # 20
    ```
- 파이썬은 오버플로우 없음 대신 속도는 C가 훨씬 빠름
- C는 메모리를 스택, 힙에 할당하지만 파이썬은 힙에만 할당(객체 기반)
- C에서 포인터를 복사하는 게 파이썬에서 리스트 참조를 복사하는 것과 비슷함
- 파이썬의 deepcopy()는 C에서 동적 메모리를 새로 할당해서 복사하는 것과 유사함


