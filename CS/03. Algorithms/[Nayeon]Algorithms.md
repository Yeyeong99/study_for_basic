# CS50 Week 3 : Algorithms 🧠

## 1️⃣ Linear Search (선형 탐색)

배열(Array)의 중요한 점 → **연속적(Contiguous)으로 저장된다.**  
즉, 배열의 요소들은 메모리에 순차적으로 배치됨.

### 📌 배열은 어떻게 동작할까?
- 배열은 **학교 사물함**과 같다. 🔒  
  → 내부를 직접 볼 수는 없지만, **index(번호)**를 통해 특정 위치에 접근 가능하다.

### 🔍 선형 탐색이란?
- 배열의 처음부터 끝까지 **순차적으로(Linear)** 원하는 요소를 찾는 방법.
- 최악의 경우, 모든 요소를 검사해야 하므로 **시간 복잡도 O(n)**.

### 🏃 탐색 과정 예시:
예제 배열:  
| 1 | 5 | 10 | 20 | 50 | 100 | 500 |
|---|---|---|---|---|---|---|

1. 찾고 싶은 숫자가 **10**이라고 가정.
2. 왼쪽부터 차례로 확인: `1 → 5 → 10`
3. 찾으면 종료! ✅ (탐색 완료)

#### ❌ 단점:
- 최악의 경우 `n`번 비교해야 함. (ex. 찾는 값이 마지막 요소일 때)
- **비효율적** (운이 좋으면 빠르게 찾지만, 그렇지 않으면 오래 걸림)

#### ✅ 장점:
- 정렬되지 않은 배열에서도 사용 가능! (binary search는 정렬 필요)
- 구현이 간단함.

---

## 2️⃣ Binary Search (이진 탐색)

📞 **두꺼운 전화번호부에서 이름을 찾을 때 쓰던 방법!**  
→ 가운데(midpoint)를 기준으로 범위를 반씩 줄여가며 탐색하는 방식.

### 🔍 이진 탐색 과정:
1. **배열이 반드시 정렬(Sorted)되어 있어야 함!**  
   (ex. `[1, 5, 10, 20, 50, 100, 500]`)
2. **중앙값(middle) 찾기**  

middle = (start + end) / 2

3. 찾고자 하는 값과 middle 비교:
- **찾는 값 < middle** → 왼쪽 절반에서 다시 탐색  
- **찾는 값 > middle** → 오른쪽 절반에서 다시 탐색  
- **찾는 값 == middle** → 탐색 종료! ✅

### 🏃 탐색 과정 예시:
찾고 싶은 값: `50`

| 1 | 5 | 10 | 20 | 50 | 100 | 500 |
|---|---|---|---|---|---|---|

1. `middle = 20` → 50은 오른쪽에 있음 → 오른쪽 절반으로 이동.
2. `middle = 100` → 50은 왼쪽에 있음 → 왼쪽 절반으로 이동.
3. `middle = 50` → 찾았다! ✅ (탐색 종료)

### ⏳ 시간 복잡도
- **O(log n)** → 매번 탐색 범위가 절반으로 줄어들기 때문.
- 데이터 개수가 많아질수록 **훨씬 빠름**!

#### ✅ 장점:
- **빠르다!** (logarithmic time complexity)
- 큰 데이터에서도 효율적.

#### ❌ 단점:
- **정렬된 배열**에서만 사용할 수 있음.
- 정렬이 필요하면 추가적인 시간(O(n log n))이 소요될 수 있음.

---

## 3️⃣ Running Time (시간 복잡도)

### ⏳ 문제 크기(size of problem)와 해결 시간(time to solve)
- 알고리즘 성능을 평가하는 기준.
- **빅-오 표기법(Big O Notation)**으로 표현.

### 📊 빅-오(Big O) 표기법

| 시간 복잡도 | 알고리즘 예시 |
|------------|------------------------|
| **O(1)**   | 해시 테이블 (Hash Table) 조회 |
| **O(log n)** | 이진 탐색 (Binary Search) |
| **O(n)**   | 선형 탐색 (Linear Search) |
| **O(n log n)** | 효율적인 정렬 알고리즘 (Merge Sort, Quick Sort) |
| **O(n²)**  | 버블 정렬(Bubble Sort), 선택 정렬(Selection Sort) |
| **O(2ⁿ)**  | 피보나치 재귀(Fibonacci using Recursion) |

### 🧐 예제 비교
- **O(n)** → 입력 크기에 비례해서 시간이 증가함. (ex. 선형 탐색)
- **O(log n)** → 입력 크기가 커져도 성능이 크게 떨어지지 않음. (ex. 이진 탐색)
- **O(n²)** → 입력 크기가 조금만 커져도 속도가 급격히 느려짐. (ex. 버블 정렬)

---

## 4️⃣ 추가 개념: Ω(오메가) 표기법 (Best Case)

- 빅-오(Big O)는 최악의 경우(Worst Case) 기준,  
반대로 오메가(Ω)는 **최상의 경우(Best Case)**를 기준으로 분석.
- 예제:
- **선형 탐색(Linear Search)**  
 - 최악: `O(n)` (마지막 요소에서 찾음)
 - 최선: `Ω(1)` (첫 번째 요소에서 찾음)
- **이진 탐색(Binary Search)**  
 - 최악: `O(log n)`
 - 최선: `Ω(1)` (첫 번째 중앙값이 정답일 경우)

---

## 🔥 정리
| 탐색 방법 | 시간 복잡도 | 장점 | 단점 |
|---------|----------|----|----|
| **선형 탐색** (Linear Search) | O(n) | 정렬 불필요, 간단 | 비효율적 |
| **이진 탐색** (Binary Search) | O(log n) | 매우 빠름 | 정렬 필요 |

- 데이터가 많을수록 **이진 탐색**을 사용하는 것이 좋음!
- 하지만 정렬이 필요하면 정렬 비용도 고려해야 함.

📌 **결론: 상황에 맞는 탐색 방법을 선택하자!** 🚀