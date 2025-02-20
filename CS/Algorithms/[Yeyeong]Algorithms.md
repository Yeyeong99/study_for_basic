# Selection Algorithm

- 주어진 자료들 중 가장 작은 값의 원소부터 차례대로 선택해 위치를 교환하는 방식(오름차순의 경우)
- 저장되어 있는 자료로부터 k번째로 큰 혹은 작은 원소를 찾는 방법
- 최소 / 최대 / 중간을 찾는 알고리즘

## 정렬 과정

- 주어진 리스트 중에서 최소값을 찾는다.
- 그 값을 리스트의 맨 앞에 위치한 값과 교환
- 맨 처음 위치를 제외한 나머지 리스트를 대상으로 위의 과정을 반복

## 선택 과정

- 정렬 알고리즘을 이용해 자료 정렬
- 원하는 순서에 있는 원소 가져오기

### 예시

- k 번째로 작은 원소를 찾을 때
  - 1번부터 k번째까지 작은 원소들을 찾아 배열의 앞쪽으로 이동, 배열의 k번째를 반환
  - k가 비교적 작을 때 유용함
  - O(kn))의 수행시간을 필요로 함

## 수도코드
```
For i from 0 to n - 1
    Find smallest number between numbers[i] and numbers[n - 1]
    Swap smallest number with numbers[i]
```

[Comparison Sorting Algorithms](https://www.cs.usfca.edu/~galles/visualization/ComparisonSort.html)


## 시간 복잡도: O(n ^ 2)
(n - 1) + (n - 2) + (n - 3) + ... + 1

= n(n - 1)/2

= (n ^ 2)/2 - n/2

= O(n ^ 2)

# Bubble Sort
## 수도 코드
```
Repeat n - 1 times
    For i from 0 to n - 2 
        If numbers[i] and numbers[i + 1] out of order
            Swap them
```
- n - 1: n 번째는 비교할 필요 없이 어차피 정렬됨
- n - 2: i 번째와 i + 1번째를 비교하기 때문에 n - 1에서 -1을 한 번 더함

### 시간복잡도: O(n ^ 2)
(n - 1) * (n - 1)

= n^2 - 2n + 1

= O(n ^ 2)

## 수도코드 2
```
Repeat n - 1 times
    For i from 0 to n - 2 
        If numbers[i] and numbers[i + 1] out of order
            Swap them
    If no Swap
        Quit
```
