# CS50 Lecture 5 - Data Structures

> ### Dictionary

- 키(Key)-값(Value) 쌍을 저장하는 자료구조로, 데이터를 빠르게 검색, 삽입, 삭제할 수 있도록 설계된 추상 자료형 구조(Abstract Data Type, ADT)

- 대표적인 구현 방법: 해시 테이블(Hash Table), 트라이(Trie)

- 주요 연산:

    삽입(Insertion) : 키-값 쌍을 추가

    검색(Lookup) : 키를 사용해 값 찾기

    삭제(Deletion) : 특정 키-값 쌍 제거

> ### Hash Table

- 데이터를 해시 함수(Hash Function)를 통해 변환한 후, 배열의 인덱스로 저장하는 방식

- 평균적으로 O(1) 시간 복잡도로 검색, 삽입, 삭제 가능

- 주요 개념:

    해시 함수(Hash Function): 입력값을 일정한 크기의 숫자로 변환하는 함수

    해시 값(Hash Value): 해시 함수의 출력값

    버킷(Bucket): 데이터를 저장하는 공간

![image](https://raw.githubusercontent.com/Y00CHAN/Images/refs/heads/master/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202025-03-06%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%208.18.36.png)

✅ 장점

- 빠른 검색 속도 (평균 O(1))

- 간결한 구현 가능

❌ 단점

- 해시 충돌 가능성

- 추가적인 메모리 사용 (버킷 할당 필요)

- 최악의 경우 검색 시간 O(n). 사실 O(n/k) 이기 때문

> ### Trie 

- 문자열을 저장하고 검색하는 데 최적화된 트리 구조

- 각 노드는 하나의 문자(Character)를 저장하며, 루트(Root)에서 자식 노드로 이동하며 문자열을 구성

- 포인터들의 모임 구조라고 이해

![image](https://raw.githubusercontent.com/Y00CHAN/Images/refs/heads/master/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202025-03-06%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%208.19.03.png)

✅ 장점

- 문자열 검색이 O(m) (m: 문자열 길이)

- 공통 접두사 저장 최적화 (메모리 절약)

❌ 단점

- 노드 수가 많아질 경우 메모리 사용량 증가

- 구현이 해시 테이블보다 복잡함

<br>

---
🔽 일상에서의 해시 테이블


![image](https://raw.githubusercontent.com/Y00CHAN/Images/refs/heads/master/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202025-03-06%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%208.20.30.png)

---
<br>

> ### Summary

- 해시 테이블은 빠른 검색을 제공하지만, 해시 충돌을 고려해야한다

- 트라이는 문자열 저장 및 검색에 최적화되어 있으며, 특히 접두사 검색이 유용

- 각각 장단점이 있으므로 상황에 따라 적절한 자료구조를 선택하는 것이 중요


