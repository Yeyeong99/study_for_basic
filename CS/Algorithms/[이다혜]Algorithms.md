# CS50_[이다혜] Algorythms

작성 일시: 2025년 2월 18일 오후 3:13

# <search.c>

### 1. `search.c`란?

**검색 알고리즘**을 구현한 C 언어 소스 코드 파일. 이 파일은 다양한 검색 기법(예: 선형 검색, 이진 검색, 해시 탐색 등)을 포함할 수 있으며, 데이터 집합에서 특정 값을 찾는 기능을 수행함.

### 2. `search.c`에서 구현할 수 있는 대표적인 검색 알고리즘

1. **선형 검색(Linear Search)**
    - 배열을 처음부터 끝까지 순차적으로 탐색하면서 원하는 값을 찾는 방식
    - 시간 복잡도: O(n)
2. **이진 검색(Binary Search)**
    - 정렬된 배열을 기준으로 중간 값을 확인하며 탐색하는 방법
    - 시간 복잡도: O(log n)
3. **해시 탐색(Hash Search)**
    - 해시 테이블을 활용하여 평균 O(1)의 빠른 검색 속도를 제공
    - 해시 함수를 사용하여 키 값을 특정 인덱스에 저장한 후 탐색하는 방식

### 선형 검색의 아이디어 구현 방법

```c
c
복사편집
#include <stdio.h>int linearSearch(int arr[], int size, int target) {
    for (int i = 0; i < size; i++) {
        if (arr[i] == target)
            return i; // 찾은 경우 인덱스 반환
    }
    return -1; // 찾지 못한 경우
}

int main() {
    int arr[] = {10, 20, 30, 40, 50};
    int target = 30;
    int index = linearSearch(arr, 5, target);
    if (index != -1)
        printf("Element found at index %d\n", index);
    else
        printf("Element not found\n");
    return 0;
}

```

### 3. `search.c`를 활용하는 분야

- 데이터베이스 검색
- 운영 체제의 프로세스 탐색
- 네트워크 라우팅 테이블 조회
- 검색 엔진의 인덱싱

### 4. 최적의 검색 알고리즘 선택법

| 알고리즘 | 정렬 필요 여부 | 평균 시간 복잡도 | 사용 예시 |
| --- | --- | --- | --- |
| 선형 검색 | 필요 없음 | O(n) | 작은 데이터셋 |
| 이진 검색 | 필요함 | O(log n) | 정렬된 데이터셋 |
| 해시 탐색 | 필요 없음 | O(1) | 빠른 검색이 필요한 경우 |

### 5. 결론

`search.c`는 다양한 검색 알고리즘을 구현하는 파일로, 데이터 검색 성능을 최적화하는 데 중요한 역할을 함. 어떤 검색 방식을 사용할지는 데이터의 크기와 특성에 따라 결정됨. 

**(C언어에서 문자를 비교할 때 알파벳 순이 아닌 아스키 문자 순서로 문자의 정수 값을 비교함. 다음주 강의에서 마저 배울건데 일단 지금은 str compare가 실제로 두 문자열을 비교하는 방법이라고 하기로 함.)**

### 1. **아스키(ASCII) 코드란?**

컴퓨터는 문자를 내부적으로 숫자로 저장. 이때 각 문자에 특정한 숫자(코드)를 부여한 것이 **ASCII(미국 표준 코드)**

- `'A'` → **65**
- `'B'` → **66**
- `'a'` → **97**
- `'b'` → **98**
- `'0'` → **48**
- `'1'` → **49**

즉, 문자들은 **알파벳 순서가 아니라, 아스키 코드 값 순서**로 저장됨

---

### 2. **아스키 순서로 비교한다는 뜻**

C 언어에서 문자를 비교할 때, 문자 자체가 아니라 **아스키 코드값(정수값)**을 기준으로 비교함

```c
c
복사편집
#include <stdio.h>int main() {
    char a = 'A';
    char b = 'a';

    if (a < b) {
        printf("A가 a보다 작습니다.\n");
    } else {
        printf("a가 A보다 작습니다.\n");
    }

    return 0;
}

```

### **결과:**

```
css
복사편집
A가 a보다 작습니다.

```

이유: `'A'`는 **65**, `'a'`는 **97**이므로 **65 < 97**이 성립하기 때문

---

### 3. **알파벳 순서 vs 아스키 순서**

알파벳 순서로 정렬하면:

```
css
복사편집
A B C D ... X Y Z a b c d ... x y z

```

하지만 아스키 순서로 보면:

```
scss
복사편집
(A=65) (B=66) ... (Z=90) (a=97) (b=98) ... (z=122)

```

즉, **대문자가 소문자보다 먼저 정렬됨**

---

### 4. **아스키 코드 기반 비교가 중요한 이유**

- C 언어에서 `if (ch1 < ch2)`와 같은 비교를 하면 **문자의 크기가 아니라 아스키 코드의 크기를 기준**으로 판단함
- 따라서 `'Z' < 'a'`는 항상 **참(true)**가 됨. (`90 < 97`)
- 배열을 정렬할 때도 아스키 코드 기준으로 동작.

**즉, 아스키 순서는 단순한 알파벳 순서와 다를 수 있으므로 이를 염두에 두고 프로그래밍해야 함!!**

# <phonebook.c>

C 언어로 작성된 전화번호부 관리 프로그램. 연락처(이름, 전화번호 등)를 저장하고 검색, 추가, 삭제하는 기능을 포함. 

<참고~>

- 전화번호 입력할 때 수학적 계산을 하지 않을 숫자들은 문자열로 처리해놓는게 좋음
- 코드 냄새(Code Smell) : 겉보기에는 작동하지만, 유지보수나 확장성이 어렵거나 비효율적인 코드 패턴.  즉, 코드 자체는 실행되지만, **가독성이 나쁘거나, 수정이 어렵거나, 비효율적인 구조를 가진 코드**

### **핵심 기능**

1. **연락처 추가**: 새로운 연락처를 입력하고 저장.
2. **연락처 검색**: 특정 이름이나 번호를 검색.
3. **연락처 삭제**: 저장된 연락처 중 특정 항목을 삭제.
4. **연락처 목록 출력**: 모든 연락처를 화면에 출력.
5. **파일 저장 및 불러오기**(선택적): 프로그램 종료 후에도 데이터 유지.

---

## **`phonebook.c` 코드 예제**

간단한 전화번호부 프로그램의 기본 구조

```c
c
복사편집
#include <stdio.h>#include <stdlib.h>#include <string.h>#define MAX_CONTACTS 100

typedef struct {
    char name[50];
    char phone[20];
} Contact;

Contact phonebook[MAX_CONTACTS];
int contact_count = 0;

void addContact() {
    if (contact_count >= MAX_CONTACTS) {
        printf("전화번호부가 가득 찼습니다!\n");
        return;
    }
    printf("이름 입력: ");
    scanf("%s", phonebook[contact_count].name);
    printf("전화번호 입력: ");
    scanf("%s", phonebook[contact_count].phone);
    contact_count++;
    printf("연락처가 추가되었습니다.\n");
}

void listContacts() {
    printf("\n=== 연락처 목록 ===\n");
    for (int i = 0; i < contact_count; i++) {
        printf("%d. %s - %s\n", i + 1, phonebook[i].name, phonebook[i].phone);
    }
}

void searchContact() {
    char search_name[50];
    printf("검색할 이름 입력: ");
    scanf("%s", search_name);

    for (int i = 0; i < contact_count; i++) {
        if (strcmp(phonebook[i].name, search_name) == 0) {
            printf("🔎 찾음: %s - %s\n", phonebook[i].name, phonebook[i].phone);
            return;
        }
    }
    printf("해당 이름의 연락처가 없습니다.\n");
}

void deleteContact() {
    char delete_name[50];
    printf("삭제할 이름 입력: ");
    scanf("%s", delete_name);

    for (int i = 0; i < contact_count; i++) {
        if (strcmp(phonebook[i].name, delete_name) == 0) {
            for (int j = i; j < contact_count - 1; j++) {
                phonebook[j] = phonebook[j + 1];
            }
            contact_count--;
            printf("연락처가 삭제되었습니다.\n");
            return;
        }
    }
    printf("삭제할 연락처를 찾을 수 없습니다.\n");
}

int main() {
    int choice;
    while (1) {
        printf("\n📞 전화번호부 메뉴\n");
        printf("1. 연락처 추가\n");
        printf("2. 연락처 목록 보기\n");
        printf("3. 연락처 검색\n");
        printf("4. 연락처 삭제\n");
        printf("5. 종료\n");
        printf("선택: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1: addContact(); break;
            case 2: listContacts(); break;
            case 3: searchContact(); break;
            case 4: deleteContact(); break;
            case 5: exit(0);
            default: printf("잘못된 선택입니다. 다시 입력하세요.\n");
        }
    }
    return 0;
}

```

---

## 🔹 **설명**

1. `Contact` 구조체를 사용해 이름과 전화번호를 저장
2. `phonebook[]` 배열에 최대 `100`개의 연락처를 저장
3. `addContact()` 새 연락처를 추가
4. `listContacts()` 저장된 연락처를 출력
5. `searchContact()` 특정 이름을 검색
6. `deleteContact()` 특정 연락처 삭제
7. `main()` 함수에서 사용자 입력을 받아 각 기능을 수행

---

## 

# <strucks 구조체>

여러 개의 변수를 하나의 데이터 구조로 묶어 관리할 수 있도록 하는 기능. 

**배열(array)과 달리 서로 다른 자료형의 변수를 하나로 묶을 수 있음.**

---

## **기본 구조**

```c
c

struct 구조체이름 {
    자료형 변수1;
    자료형 변수2;
    ...
};

```

- `struct` 키워드를 사용하여 구조체를 선언
- 여러 개의 변수(멤버 변수) 포함 가능
- `int`, `float`, `char` 등 서로 다른 자료형을 조합 가능

---

## **기본적인 구조체 예제**

```c
c
복사편집
#include <stdio.h>// 구조체 정의
struct Person {
    char name[50];
    int age;
    float height;
};

int main() {
    // 구조체 변수 선언
    struct Person person1 = {"홍길동", 25, 175.5};

    // 구조체 값 출력
    printf("이름: %s\n", person1.name);
    printf("나이: %d\n", person1.age);
    printf("키: %.1f cm\n", person1.height);

    return 0;
}

```

🔹 **출력 결과**

```
makefile
복사편집
이름: 홍길동
나이: 25
키: 175.5 cm

```

---

## **구조체의 활용**

### **1) 구조체 배열**

같은 형식의 여러 데이터를 저장할 때 사용

### **2) 구조체 포인터**

구조체를 포인터로 다룰 수도 있음. `->` 연산자를 이용하여 멤버 접근 가능

### **3) typedef를 이용한 구조체 간단화**

매번 struct를 사용하는게 불편하다면 `typedef`를 사용하면 **구조체의 별칭을 만들어 코드가 깔끔해짐** 

```c
c
복사편집
#include <stdio.h>// typedef 사용
typedef struct {
    char name[30];
    int age;
} Person;

int main() {
    Person p1 = {"김민수", 27};

    printf("이름: %s\n", p1.name);
    printf("나이: %d\n", p1.age);

    return 0;
}

```

📌 `typedef`를 사용하면 `struct Person` 대신 `Person`만 써도 됨

---

### **4) 구조체 안에 구조체 포함**

구조체 내부에 또 다른 구조체를 포함할 수도 있음. 

---

# <sorting>

청중 중에서 자원봉사자 받아서 사람들을 정렬시키며 설명. 이 다음 파트가 버블 정렬과 선택 정렬인데 일단 간단히 정리는 해놓겠음. 

**정렬은 데이터를 특정 기준(오름차순, 내림차순..) 으로 정리하는 과정. 정렬 알고리즘은 시간 복잡도와 메모리 사용량을 고려하여 다양한 방식으로 구현됨.**

---

## **정렬 알고리즘의 분류**

### 🔹 **비교 기반 정렬 (Comparison-based Sorting)**

- 두 개의 데이터를 비교하여 정렬하는 방식
- 예시: **버블 정렬, 선택 정렬, 삽입 정렬, 병합 정렬, 퀵 정렬, 힙 정렬**

### 🔹 **비교 없이 정렬 (Non-comparison Sorting)**

- 특정한 조건(숫자의 자릿수, 범위 등)을 이용하여 정렬
- 예시: **계수 정렬, 기수 정렬, 버킷 정렬**

---

## 1️⃣ **버블 정렬 (Bubble Sort)**

💡 **개념**: 인접한 두 개의 요소를 비교하여 큰 값을 뒤로 보내는 방식

🔹 **시간 복잡도**: O(𝑛²) (비효율적)

```c
c
복사편집
#include <stdio.h>void bubbleSort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) { // 오름차순 정렬
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}

void printArray(int arr[], int n) {
    for (int i = 0; i < n; i++) printf("%d ", arr[i]);
    printf("\n");
}

int main() {
    int arr[] = {5, 2, 9, 1, 5, 6};
    int n = sizeof(arr) / sizeof(arr[0]);
    bubbleSort(arr, n);
    printArray(arr, n);
    return 0;
}

```

📌 **특징**: 단순하지만 매우 비효율적, 작은 데이터에만 적합

---

## 2️⃣ **선택 정렬 (Selection Sort)**

💡 **개념**: 가장 작은 요소를 찾아 앞으로 이동

🔹 **시간 복잡도**: O(𝑛²) (비효율적)

```c
c
복사편집
void selectionSort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        int minIdx = i;
        for (int j = i + 1; j < n; j++) {
            if (arr[j] < arr[minIdx]) minIdx = j;
        }
        int temp = arr[i];
        arr[i] = arr[minIdx];
        arr[minIdx] = temp;
    }
}

```

📌 **특징**: 교환 횟수가 적지만 여전히 O(𝑛²)이라 비효율적

---

## **정렬 알고리즘 성능 비교**

| 알고리즘 | 평균 시간복잡도 | 최악 시간복잡도 | 특징 |
| --- | --- | --- | --- |
| **버블 정렬** | O(𝑛²) | O(𝑛²) | 매우 비효율적 |
| **선택 정렬** | O(𝑛²) | O(𝑛²) | 작은 데이터에 적합 |
| **삽입 정렬** | O(𝑛²) | O(𝑛²) | 데이터가 거의 정렬된 경우 효율적 |
| **퀵 정렬** | O(𝑛 log 𝑛) | O(𝑛²) | 평균적으로 가장 빠름 |
| **병합 정렬** | O(𝑛 log 𝑛) | O(𝑛 log 𝑛) | 추가 메모리 필요 |
| **계수 정렬** | O(𝑛 + k) | O(𝑛 + k) | 정수 정렬에 최적 |