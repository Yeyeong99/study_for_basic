# Standard C로 get_string 생성

## 숫자 받고 출력

```c
#include

int main(void)
{
    int n;
    printf("n: ");
    scanf("%i", &n); // address of n
    print("n: %i\n", n);
}
```

## 문자열 출력

```c
#include

int main(void)
{
    char *s;
    printf("s: ");
    scanf("%s", s);
    printf("s: %s\n", s);
}
```

### 입력

```
HI!
```

### 결과

```
Segmentation fault(cord dumped)
```

## 문제 상황

- 숫자를 메모리에 저장할 때: 4바이트만 차지, 메모리가 고정되기 때문에 문제될 게 없음
- char \*s
  - 문자열이 저장된 메모리의 시작 주소를 보관하는 포인터
    - 하지만 초기화되지 않음 = 변수에 값이 할당되지 않음 = s가 어떤 메모리를 가리키는지 알 수 없음
      - 이 경우 garbage value를 가지고 있거나(아무것도 가리키지 않거나) 잘못된 주소를 가리킬 수 있음
        - garbage value를 가질 경우 이 포인터가 가리키는 메모리가 유효한 메모리인지 아닌지 알 수 없음
  - scanf("%s", s); 실행되면 입력 받은 문자열을 그 garbage value가 가리키는 메모리에 저장하려고 함.
  - 하지만 해당 메모리는 존재하지 않거나 접근이 불가능. 따라서 segmentation fault가 나옴

### 해결 방법

```c
char s[100];  // 충분한 크기의 배열
scanf("%s", s);

char *s = malloc(100 * sizeof(char));  // 동적 메모리 할당
scanf("%s", s);
```

### s에 길이를 할당할 경우

```c
#include

int main(void)
{
    char s[4];
    printf("s: ");
    scanf("%s", s);
    printf("s: %s\n", s);
}
```

### 입력

```
HI!
```

### 결과

```
HI!
```

- 오류는 안나지만 입력되는 string이 길어진다면

### 결과

```
Segmentation fault (core dumped)
```

## cs50의 get_string의 원리

1. 입력한 문자를 하나씩 받음: 하나의 character가 들어옴
2. 다른 character가 들어오는지 확인: 입력이 완료되지 않을 경우, 계속해서 다음 문자가 입력되는지를 확인함. 이 과정에서 enter를 치면 입력이 끝난 것으로 처리 됨
3. 들어올 때마다 메모리를 할당함: 각 문자를 저장할 메모리를 동적으로 할당함. 처음에는 작은 크기의 메모리 블록을 할당, 추가 문자가 들어오면 `malloc`을 이용해 필요한 만큼 메모리 크기를 늘려가면서 메모리를 동적으로 할당함

# file I/O (Input / Output)

## file 관련 함수

- fopen : open a file
- fclose: close a file
- fprintf: print something not on a screen but via a file

## phonebook.c

```c
#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    FILE *file = fopen("phonebook.csv", "a"); // add, not overwriting

    string *name = get_string("Name: ");
    string *number = get_string("Number: ");

    fprintf(file, "%s, %s\n", name, number);

    fclose(file);
}
```

- string *name, string *number인 이유
  - get_string은 동적으로 할당된 메모리 주소를 반환하기 때문에, name과 number는 해당 메모리를 가리키는 포인터가 되어야 함

    > 참고
    >
    > - get_string은 사용자가 입력한 문자열을 반환하는 함수
    >   - 반환 값의 타입은 string
    >     - CS50 라이브러리에서 string은 char \*로 정의됨 = get_string은 문자열을 가리키는 포인터를 반환

### 결과

- phonebook.csv 파일이 생성, 입력된 내용이 저장됨

```c
#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    FILE *file = fopen("phonebook.csv", "a"); // add, not overwriting
    if (file == NULL) // prevent errors
    {
        return 1;
    }
    string *name = get_string("Name: ");
    string *number = get_string("Number: ");

    fprintf(file, "%s, %s\n", name, number);

    fclose(file);
}
```

## copy.c

```c
#include <stdio.h>
#include <stdint.h>

typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
    FILE *src = fopen(argv[1], "rb") //read binary
    FILE *dst = fopen(argv[2], "wb") //write

    BYTE b;

    // src의 내용을 dst에 복사하기
    while (fread(&b, sizeof(b), 1, src) != 0)
    {
        fwrite(&b, sizeof(b), 1, dst);
    }

    fclose(dst);
    fclose(src);
}
```
### 코드 흐름
1. 사용자로부터 파일 경로 두 개를 입력받음 첫 번째는 **소스 파일** (읽을 파일), 두 번째는 **목적지 파일** (쓰게 될 파일).
2. 소스 파일와 목적지 파일을 바이너리 모드로 연다.
3. 소스 파일에서 1바이트씩 읽어 들여서, 그 데이터를 목적지 파일에 쓰는 식.
4. 파일 끝까지 반복하여 복사한 후, 파일을 닫음.

### 코드 설명

1. **`typedef uint8_t BYTE;`**
    ```c
    typedef uint8_t BYTE;
    ```
    - `uint8_t`는 `stdint.h`에서 제공하는 1바이트 크기의 부호 없는 정수 타입
    - `BYTE`는 `uint8_t`의 별칭, 코드에서 1바이트 크기의 데이터를 다룰 때 `BYTE`를 사용할 것.

2. **`main` 함수**
    ```c
    int main(int argc, char *argv[])
    ```
    - `argc`: 프로그램 실행 시 입력된 인자의 개수
    - `argv`: 입력된 인자들의 문자열 배열.`argv[1]`은 소스 파일 경로, `argv[2]`는 목적지 파일 경로

4. **파일 열기**
    ```c
    FILE *src = fopen(argv[1], "rb");  // read binary
    FILE *dst = fopen(argv[2], "wb");  // write binary
    ```
    - `fopen(argv[1], "rb")`: `argv[1]`로 지정된 파일을 바이너리 모드로 읽기 전용으로 엶.
    - `fopen(argv[2], "wb")`: `argv[2]`로 지정된 파일을 바이너리 모드로 쓰기 전용으로 엶.
    - `"rb"`: 바이너리 모드로 읽기.
    - `"wb"`: 바이너리 모드로 쓰기.

5. **파일 복사 작업**
    ```c
    BYTE b;
    ```
    - `BYTE b`: 파일에서 읽어온 1바이트 데이터를 저장할 변수
    
    ```c
    while (fread(&b, sizeof(b), 1, src) != 0)
    {
        fwrite(&b, sizeof(b), 1, dst);
    }
    ```
    - &b: b의 메모리 주소 나타냄
        - BYTE b;에서 &b는 b 변수가 저장된 메모리 위치를 가리키는 값
        - 이 주소를 다른 변수에 저장하거나 포인터에 전달할 수 있음
    - `fread(&b, sizeof(b), 1, src)`: `src` 파일에서 1바이트씩 읽어서 `b`에 저장. `fread`는 파일에서 데이터를 읽을 때 사용하며, 파일의 끝에 도달할 때까지 반복.
    - `fwrite(&b, sizeof(b), 1, dst)`: `b`에 저장된 1바이트 데이터를 `dst` 파일에 씀.
    - `fread`가 반환하는 값이 0이면 (즉, 파일 끝에 도달하면) `while` 루프가 종료.

6. **파일 닫기**
    ```c
    fclose(dst);
    fclose(src);
    ```
    - `fclose`: 파일을 닫고, 파일 작업을 종료. `fclose`는 열었던 파일 포인터를 닫고, 파일 시스템 리소스를 해제함.


### 특성
- **파일 크기가 큰 경우에도 제대로 작동**. 왜냐하면 한 번에 1바이트씩 읽고 쓰기 때문에 메모리 사용이 최소화됨
- 프로그램은 **바이너리 파일**을 다루기 때문에 텍스트 파일과 달리 줄바꿈 문자 등을 자동으로 변환하지 않는다. 따라서 원본 파일의 내용이 그대로 복사됨.
    - 바이너리 모드는 파일을 이진 데이터 형식으로 읽거나 쓰는 모드
        - 이미지 파일, 비디오 파일, 실행 파일 등과 같이 문자열 외의 데이터를 다루는 경우 사용됨
        - cf) 텍스트 모드 ("r", "w", "a"), 텍스트 파일 다룰 때 주로 사용

