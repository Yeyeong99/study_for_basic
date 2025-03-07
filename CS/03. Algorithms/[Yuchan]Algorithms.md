# CS50 Lecture 3 - Algorithms

> ### Recursion

- 함수가 자기 자신을 호출하는 프로그래밍 기법
- 기본 사례 (Base Case)와 재귀 사례 (Recursive Case)로 구성
- 적절한 종료 조건(Base Case)이 없으면 **무한 루프** 발생

#### Factorial 구현 (재귀 vs 반복문)

``` c
// 반복문 방식
void draw(int n)
{
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < i + 1; j++)
        {
            printf("#");
        }
        printf("\n");
    }
}
```

```c
// 재귀 방식
void draw(int n) 
{
    if (n <= 0) 
    {
    return; // Base case
    }
    
    draw(n - 1); // 재귀 호출로 위쪽부터 출력
    
    for (int i = 0; i < n; i++)
    {
    printf("#"); 
    }
    printf("\n");
}
```

#### Call Stack & Recursion
- 함수 호출이 발생할 때마다 **Call Stack**에 새로운 프레임이 추가
- Base Case에 도달하면, 스택이 역순으로 해제되며 함수가 종료
- 너무 깊은 재귀 호출은 **Stack Overflow**를 유발할 수 있음

> ### Merge Sort

- **분할 정복 (Divide and Conquer)** 알고리즘의 대표적인 예제
- 배열을 반으로 나누고, 각 부분을 정렬한 후 합병(Merge)하는 방식
- **시간 복잡도: O(n log n)** (항상 일정한 성능 보장)

#### Merge Sort 단계
1. **Divide (분할)**: 배열을 절반으로 나눔
2. **Conquer (정복)**: 각각의 절반을 재귀적으로 정렬
3. **Merge (합병)**: 두 개의 정렬된 배열을 하나의 정렬된 배열로 합침

#### Merge Sort 구현
```
If only one number // Base case
    Quit
Else
    Sort left half of numbers
    Sort right half of numbers
    Merge sorted halves
```
![image](https://raw.githubusercontent.com/Y00CHAN/Images/refs/heads/master/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202025-02-19%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%208.50.57.png)

#### Merge Sort 특징
- **장점**
  - 최악, 평균, 최선의 경우 모두 **O(n log n)** 보장
  - 안정 정렬(Stable Sort): 동일한 값의 원소 순서 유지
- **단점**
  - 추가적인 메모리 공간이 필요 (O(n) 수준의 보조 배열 필요)
  - 작은 배열에서는 Quick Sort보다 느릴 수 있음

> ### Summery
> 
| 개념         | 설명 |
|-------------|--------------------------------------------|
| Recursion   | 함수가 자기 자신을 호출하는 개념. Base Case 필요 |
| Call Stack  | 재귀 호출 시 사용되는 스택 구조. Stack Overflow 주의|
| Merge Sort  | Divide & Conquer 방식의 정렬 알고리즘. O(n log n) |
| Merge 단계  | 두 개의 정렬된 배열을 하나로 합치는 과정 |

#### 정렬 알고리즘 비교
| 정렬 알고리즘 | 평균 시간복잡도 | 최악 시간복잡도 | 공간복잡도     |
|-------------|--------------|--------------|-----------|
| Bubble Sort | O(n²)        | O(n²)        | O(1)      |
| Insertion Sort | O(n²)    | O(n²)        | O(1)      |
| Merge Sort  | O(n log n)   | O(n log n)   | O(n)      |
| Quick Sort  | O(n log n)   | O(n²)        | O(log n)  |

- **Recursion**: Base Case 필수! Call Stack 주의
- **Merge Sort**: 안정 정렬, O(n log n), 하지만 추가 메모리 사용
- **Merge 과정**이 핵심. 정렬된 배열을 효율적으로 합치는 것이 중요
