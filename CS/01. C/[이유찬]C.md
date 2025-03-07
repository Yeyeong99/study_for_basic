# CS50 Lecture 1 - C

> ### C

- C 언어는 시스템 프로그래밍 및 일반적인 소프트웨어 개발에 널리 사용되는 프로그래밍 언어

- 절차지향적(Procedural), 메모리 관리가 자유로운 저수준(low-level) 언어

- 컴파일 언어로, C 코드는 기계어로 변환되어 실행

> ### Compile

![Compile](https://raw.githubusercontent.com/Y00CHAN/Images/refs/heads/master/%E1%84%8F%E1%85%A5%E1%86%B7%E1%84%91%E1%85%A1%E1%84%8B%E1%85%B5%E1%86%AF.png)
- 소스코드를 입력받아 머신코드로 출력을 내보내는 일종의 프로그램

- 소스코드를 C, Python, Java 등으로 작성 후 컴파일러를 통해 0과 1의 조합으로 이해되는 머신코드로 번역

> ### printf

```c
#include <stdio.h>

int main(void)
{
    printf("hello, world\n");
    return 0;
}
```

> ### if, else

- 조건에 따라 프로그램이 다른 동작 수행

```c
#include <stdio.h>

int main(void)
{
    int x = 5;
    if (x < 10)
    {
        printf("x is less than 10\n");
    }
    else
    {
        printf("x is 10 or more\n");
    }
    return 0;
}
```

> ### for, while

- 코드를 반복 실행

```c
#include <stdio.h>

int main(void)
{
    for (int i = 0; i < 3; i++)
    {
        printf("meow\n");
    }
    return 0;
}
```

> ### Function

- 코드를 모듈화하여 재사용

```c
#include <stdio.h>

void meow(void)
{
    printf("meow\n");
}

int main(void)
{
    for (int i = 0; i < 3; i++)
    {
        meow();
    }
    return 0;
}
```

---

> ### Summary

- C 언어는 강력하고 유연한 저수준 프로그래밍 언어
- 변수와 데이터 타입을 사용하여 데이터를 저장하고 처리
- `printf`, `scanf`로 입출력을 수행
- 조건문과 반복문을 사용하여 프로그램의 흐름을 제어
- 함수를 사용하여 코드를 구조화하고 재사용

> ### Questions

- C에서 void 키워드란? 어떤 상황에서 사용되는가
- 제어문에서 for vs while 루프 성능차이
- 절차지향 객체지향 차이, 예시

> ### NOTE

- CS50 라이브러리 사용 개발환경 구축, 이후 예제 실습










