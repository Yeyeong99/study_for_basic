# CS50 WEEK 2: Arrays

## compile

### 🔎 Comparison Table: Clang vs. Make

| Feature                 | **Clang** (Compiler)                                       | **Make** (Build System)                                 |
| ----------------------- | ---------------------------------------------------------- | ------------------------------------------------------- |
| **Purpose**             | Converts C source code into machine code                   | Automates the compilation process                       |
| **Main Role**           | Compiles `.c` files into executables                       | Runs Clang (or GCC) automatically based on dependencies |
| **Usage**               | Used to compile a single C file or multiple files manually | Used to compile **complex projects** with many files    |
| **Command Example**     | `clang hello.c -o hello`                                   | `make hello` (Uses a **Makefile**)                      |
| **Dependency Handling** | Does not track dependencies                                | Tracks **which files need recompilation** (saves time)  |
| **Configuration File?** | ❌ No configuration file needed                            | ✅ Uses a **Makefile** to define compilation rules      |
| **Recompilation**       | Recompiles everything each time                            | Only recompiles **modified files**                      |
| **Best For**            | Small programs with a few `.c` files                       | Large projects with multiple `.c` and `.h` files        |

- Clang : when using Clang alone, the compiler doesn't know whether a file has changed or not. It recompiles all files every time, even if only one file was modified.

### 우리가 `컴파일`이라고 부르는 것은 사실상 네 단계로 나뉜다.

> preprocessing compiling assembling linking

1. preprocessing: convert # include lines into equivalents, #include <cs50.h>: 내부에 있는 프로토타입을 불러오는 것

2. compiling: c ▶ assembly codes
3. assembling: assembly codes ▶ 0, 1
4. linking: combine all the files

## Debugging

```c
#include <cs50.h>
#include <stdio.h>

void print_column(int height);

int main(void)
{
    int h = get_int("Height: ");
    print_column(h);
}

void print_column(int height)
{
    for (int i = 0; i <= height; i++)
    {
        printf("#\n");
    }
}
```

- debug50: find programmatic errors
  ```
  debug50 ./file_name
  ```
  - this will ask where you want to pause
  - click a red dot on the left side
  - good to see what happens in loops

## Arrays

```c
int scores[3]; //1

scores[0] = 72;
scores[1] = 73;
scores[2] = 33;

```

- 1: 3개의 integer를 담을 array를 선언

```c
#include <cs50.h>
#include <stdio.h>

// const int N = 3; //1


int main(void)
{
    const int N = 3;
    int scores[N];
    for (int i = 0; i < N; i++)
    {
        scores[i] = get_int("Score: ");
    }
    printf("Average: %f\n", (score[0] + score[1] + scores[2]) / (float) N);
}
```

- 1: global variable

## String

```C
#include <cs50.h>
#include <stdio.h>

int main(void)
{
    string s = "Hi!";

    printf("%s\n", s); // Hi!
    printf("%c%c%c\n", s[0], s[1], s[2]); // Hi!
    printf("%i%i%i\n", s[0], s[1], s[2], s[3]); //72 73 33 0
}
```

- Nul 바이트: string의 맨 마지막에는 꼭 0으로만 이뤄진 값이 있음. 스트링이 끝나는 것을 알리기 위해
  쓰이는 값.

```c
#include <cs50.h>
#include <stdio.h>

int main(void)
{
    string words[2];

    words[0] = "Hi!";
    words[1] = "Bye!";

    printf("%s\n", words[0]); // Hi!
    printf("%s\n", words[1]); // Bye!

    printf("%c%c%c\n", words[0][0], word[0][1], word[0][2]); // Hi!
    printf("%c%c%c%c\n", words[1][0], word[1][1], word[1][2]); // Bye!
}
```

### String Length

```c
#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    string name = get_string("Name: "); //David

    int n = 0;
    while (name[n] != '\0') //1
    {
        n++;
    }
    printf("%i\t", n) // 5

    int length = strlen(name); //string.h에 있음
    printf("%i", length) // 5



}
```

- 1: `'\0'`: Nul 값을 가리킴

```c
#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    string s= get_string("Input: ")
    printf("Output: ");

    for (int i = 0, length = strlen(s); i < n; i++)
    {
        printf("%c", s[i]);
    }
    print("\n");
}
```
## Command Line Argument

`void` → int argc, string argv[]와 같이 변경 가능

### file greet.c

```c
#include <cs50.h>
#include <stdio.h>

int main(void)
{
    string answer = get_string("What's your name?: ");
    printf("Hello, %s\n", answer);
  
}
```

```
// terminal
$ make greet
$ ./greet
What's your name? David
Hello, David
$
```

### command line argument 사용

```c
#include <cs50.h>
#include <stdio.h>

int main(int argc, string argv[])
{
    printf("Hello, %s\n", argv[1]);
}
```

```
// terminal
$ make greet
$ ./greet David
Hello, David
$
```

- argc : 넘어온 인자의 수를 저장
- argv[0]: 파일 이름을 가리킨다
    - 1부터가 사람이 직접 작성하는 변수
    - 만약 변수를 하나만 입력했다면 argv[2]로 바꿀 경우 아무것도 출력되지 않음
        - if문으로 처리 가능

![IMG_5050.jpeg](attachment:05a200e5-ba4f-4dc7-9a85-c194eac7dcb3:IMG_5050.jpeg)

이런 것도 할 수 있다: Rawr 부분이 command line argument

## exit status

- 인터넷에서 404: 주소가 잘못됨

```c
#include <cs50.h>
#include <stdio.h>

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Missing command-line argument\n");
        return 1
    }
    printf("Hello, %s\n", argv[1]);
    return 0;
}
```

```
// terminal
$ make greet
$ ./greet David
Hello, David
$ echo $?
0
$ ./greet David May
Missing command-line argument
$ echo $?
1
```

- echo $? return 값을 볼 때 사용

## Cryptography

plain text → cipher → ciphertext

- plain text 에 key 가 같이 들어감
- 시저 암호: 영어 알파벳을 뒤로 n개 옮기는 식  ex) Hi → Ij