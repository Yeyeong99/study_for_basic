# CS50 Memory 정리

## Pointer Arithmetic (포인터 연산)

포인터를 사용하면 배열 인덱스 표기 대신 간접 참조 연산(`*`)을 활용하여 메모리에 접근할 수 있습니다.

```cpp
#include <stdio.h>

int main(void)
{
    char *s = "HI!";
    printf("%c", s[0]);
    printf("%c", s[1]);
    printf("%c", s[2]);
}
```

위의 코드는 배열 인덱스(`s[0]`, `s[1]`, `s[2]`)를 사용하여 문자에 접근합니다. 하지만, 같은 동작을 포인터 연산을 활용해 다음과 같이 표현할 수도 있습니다.

```cpp
#include <stdio.h>

int main(void)
{
    char *s = "HI!";
    printf("%c", *s);         // s[0]과 동일
    printf("%c", *(s + 1));   // s[1]과 동일
    printf("%c", *(s + 2));   // s[2]과 동일
}
```

## 💡 포인터 연산의 원리
- `s`는 문자열 "HI!"의 첫 번째 문자를 가리키는 포인터입니다.
- `s + 1`은 `s`가 가리키는 주소에서 한 바이트(1 char) 앞으로 이동한 주소입니다.
- `*(s + 1)`은 이동한 주소에 저장된 문자를 참조합니다.
- 따라서 배열 표기법 대신 포인터 연산을 활용하면 더 간결한 코드를 작성할 수 있습니다.

---

## String Comparison (문자열 비교)

```cpp
#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    char *s = get_string("s: ");
    char *t = get_string("t: ");

    if (strcmp(s, t) == 0)
    {
        printf("Same\n");
    }
    else
    {
        printf("Different\n");
    }
}
```

### ❓ 왜 `s == t` 비교에서 항상 `Different`가 나오는가?
- 변수 `s`와 `t`는 문자열이 아니라 **문자열이 저장된 메모리의 주소를 가리키는 포인터**입니다.
- `get_string()`이 호출될 때마다 새로운 메모리 공간이 할당되므로, 설령 같은 문자열을 입력하더라도 `s`와 `t`는 서로 다른 주소를 가리킵니다.

---

## Copying (문자열 복사)

```cpp
#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>
#include <string.h>

int main(void)
{
    char *s = get_string("s: ");
    char *t = malloc(strlen(s) + 1);
    if (t == NULL)
    {
        return 1;
    }
    strcpy(t, s);
    t[0] = toupper(t[0]);

    printf("Original: %s\n", s);
    printf("Copied: %s\n", t);

    free(t);
}
```

### 🔥 `malloc`과 `free`란?
- `malloc(size)`: 주어진 바이트 크기만큼 **힙(Heap) 메모리**에 동적 할당
- `free(ptr)`: `malloc`으로 할당된 메모리를 해제
- 동적으로 할당된 메모리는 `free()`를 호출하지 않으면 프로그램 종료 후에도 해제되지 않아 **메모리 누수(memory leak)** 가 발생할 수 있음.

---

## malloc and Valgrind (메모리 할당과 검증)

다음 코드에서 `malloc`을 사용하여 동적 메모리를 할당합니다.

```cpp
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int *x = malloc(3 * sizeof(int));

    x[0] = 72;
    x[1] = 73;
    x[2] = 33;

    free(x);
}
```

### 🛑 메모리 누수 (Memory Leak)
위 코드에서 `free(x);`를 제거하면 **메모리 누수**가 발생합니다. 이를 방지하려면 **Valgrind**를 사용하여 디버깅할 수 있습니다.

```sh
valgrind ./memory
```

#### 출력 예시:
```
==1234== 12 bytes in 1 blocks are definitely lost in loss record 1 of 1
==1234== LEAK SUMMARY:
==1234==    definitely lost: 12 bytes in 1 blocks
```

### 📌 `free()`를 반드시 사용해야 하는 이유
- `malloc()`으로 동적으로 할당한 메모리는 프로그램 종료 후에도 해제되지 않습니다.
- **메모리 누수가 발생하면 프로그램이 실행될수록 사용 가능한 메모리가 줄어들어 성능 저하 및 충돌(crash)이 발생할 수 있습니다.**
- **해결 방법:**
  - `free(x);`를 호출하여 할당된 메모리를 해제합니다.
  - `malloc()`을 여러 번 호출한 경우, 사용이 끝난 모든 메모리를 `free()`해야 합니다.

---

## 결론
- 포인터 연산을 활용하면 배열보다 효율적으로 메모리에 접근 가능.
- 문자열 비교 시 `==`가 아닌 `strcmp()` 사용.
- 새로운 문자열을 만들려면 `malloc()`을 이용해 별도의 메모리 할당 필요.
- `malloc()`으로 할당한 메모리는 반드시 `free()`로 해제해야 함.
- `valgrind`를 사용하여 메모리 누수를 디버깅 가능.

---