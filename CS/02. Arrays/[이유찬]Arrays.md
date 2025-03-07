# CS50 Lecture 2 - Arrays [Strings]

> ### Strings

| H   | I   | !   | \0  |
|-----|-----|-----|-----|
| 72  | 73  | 33  | 0   |
|01001000|01001001|00100001|00000000|


- 각 문자는 ASCII 코드로 저장되며, 마지막 문자는 문자열의 종료를 알리는 값 00000000 -> \0 -> NUL

- 사람의 바이트로는 H, I, ! 으로 3 바이트이지만 컴퓨터의 바이트로는 여분의 공간을 포함해 4 바이트

- 이런 구조는 다른 언어와는 다르다. 다른 언어에서는 더 강력하고 C에서는 이런 방식.

```c
#include <cs50.h>
#include <stdio.h>

int main(void)
{
    string s = "HI!";

    printf("%i %i %i\n", s[0], s[1], s[2]); // 72 73 33
    printf("%i %i %i %i\n", s[0], s[1], s[2], s[3]); // 72 73 33 0
}
```

> ### String Length

- 문자열의 길이를 계산하기 위해서는 널 종단 문자를 만날 때까지 문자의 개수를 세어야 한다. 이를 위해 `string_length` 함수를 다음과 같이 정의.

```c
#include <cs50.h>
#include <stdio.h>

int main(void)
{
    string name = get_string("Name: "); // Ychan

    int n = 0;
    while (name[n] != '\0') // 문자 위치가 \0과 같아질때까지 n++
    {
        n++; 
    }
    printf("%i\n", n); // 5
}
```

- 내장함수 strlen
```c
#include <string.h> // string 라이브러리
lenght = strlen(name);
```

> ### uppercase.c

- 소문자를 대문자로 만드는 코드를 짜보자.

```c
#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    string s = get_string("Before: ");
    printf("After:  ");
    // 문자열의 길이를 계산하고 반복문을 실행
    for (int i = 0, n = strlen(s); i < n; i++)
    {
        // 만약 현재 문자가 소문자(a~z)라면
        if (s[i] >= 'a' && s[i] <= 'z')
        {
            // 대문자로 변환하여 출력 (ASCII 코드에서 소문자 - 32 = 대문자)
            printf("%c", s[i] - 32);
        }
        else
        {
            // 소문자가 아니면 그대로 출력
            printf("%c", s[i]);
        }
    }
    printf("\n");
}
```

- 내장함수 toupper
```c
#include <ctype.h> // ctype 라이브러리
printf("%c", toupper(s[i]));
```

> Python에서...
- upper()는 Python의 C 언어로 구현된 내부 함수(PyUnicode_ToUppercase())를 호출해서 실행된다.

- 직접 구현하면 구조는 똑같다.
```py
def fast_upper(s):
    result = [chr(ord(char) - 32) if 'a' <= char <= 'z' else char for char in s]
    return "".join(result)
```
- ord() : 문자의 ASCII 코드 가져오는 함수
- chr() : ASCII 숫자에 해당하는 문자를 가져오는 함수

> ### Summary

- 결국 String도 컴퓨터 내부에서는 숫자의 Array
- 그렇기 때문에 문자의 해당 코드를 가져와서 여러가지 작업을 수행할 수 있음
- C에서 모든 문자열의 마지막에는 여분의 바이트 NUL(\0)이 존재, 문자열의 끝을 인식함





