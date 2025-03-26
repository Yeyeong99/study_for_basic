# Index

## 예시 1

### 인덱스를 사용하지 않은 경우

```sql
sqlite> .timer ON
sqlite> SELECT * FROM shows WHERE title = 'The Office";
```

- `.timer ON` 걸리는 시간을 볼 수 있음
  - 0.044초 정도 걸림 (linear search)
- 확인해보면 시간이 길게 걸리진 않지만, 더 빠르게 조회할 수 있는 방법이 있다.

### 인덱스 사용한 경우

```sql
sqlite> CREATE INDEX title_index ON shows (title);
sqlite> SELECT * FROM shows WHERE title = 'The Office";
```

- 0.00초로 바뀜
- imdb.com 같이 실제 서비스를 하며 규모가 커질 경우 유용 (B tree)

## 참고) B tree

> ![alt text](./Yeyeong_images/image.png)

**B-Tree**(Balanced Tree)는 **데이터베이스와 파일 시스템에서 인덱스를 효율적으로 관리하기 위해 사용되는 트리 구조**이다. 특히, **SQL에서 인덱스를 구현할 때 사용되는 자료구조 중 하나**이다.

### **특징**

1. **균형 잡힌 트리 (Balanced Tree)**

   - 모든 리프 노드가 같은 깊이에 존재하여, 검색 속도가 일정하다.
   - 편향 트리(Skewed Tree)와 달리 특정 경우에 성능 저하가 발생하지 않는다.

2. [**다중 노드 (Multi-way Tree)**](#특징)

   - 일반적인 이진 탐색 트리(Binary Search Tree, BST)와 다르게 **각 노드가 여러 개의 자식 노드를 가질 수 있다.**
   - 이를 통해 **트리의 높이를 낮춰(=무언가 찾아야할 때 들어가는 step의 수가 줄어듦) 디스크 I/O(디스크에서의 Input, Output(읽고 쓰는 작업))를 줄일 수 있다.** (DB 성능 최적화)

3. **삽입과 삭제가 균형 유지됨**

   - 새 데이터를 삽입하거나 삭제할 때, 자동으로 균형을 유지하여 **O(log N)**의 성능을 보장한다.

4. **SQL 인덱스에서 사용됨**
   - **B-Tree는 일반적인 SQL 인덱스(B-Tree Index)에서 많이 사용된다.**
   - `CREATE INDEX`로 생성하는 기본 인덱스는 대부분 B-Tree 구조이다.

---

### **B-Tree vs B+Tree**

B-Tree와 함께 많이 비교되는 것이 **B+Tree**이다.

| 비교 항목       | B-Tree                | B+Tree                                  |
| --------------- | --------------------- | --------------------------------------- |
| **데이터 저장** | 모든 노드에 저장 가능 | 리프 노드에만 저장                      |
| **탐색 속도**   | 느릴 수 있음          | 더 빠름                                 |
| **범위 검색**   | 느림                  | 빠름 (리프 노드가 연결 리스트로 연결됨) |
| **사용처**      | 파일 시스템           | 데이터베이스 인덱스                     |

- **SQL에서는 B+Tree가 더 많이 사용됨.**
  - 이유: **범위 검색이 빠르고** 디스크 I/O가 적기 때문.

---

### **B-Tree 기반 SQL 인덱스 예시**

```sql
-- 인덱스 생성 (기본적으로 B-Tree 인덱스)
CREATE INDEX idx_user_name ON users(name);

-- 인덱스를 활용한 검색 (빠르게 수행됨)
SELECT * FROM users WHERE name = 'Alice';
```

### **정리**

✅ B-Tree는 **SQL에서 기본적으로 사용되는 인덱스 자료구조**  
✅ **균형 유지**로 인해 검색, 삽입, 삭제 속도가 **O(log N)**  
✅ **B+Tree**는 B-Tree보다 **범위 검색이 빠르고** 더 많이 사용됨

## 예시 2)

### 여러 데이터베이스를 함께 활용하지만, Index를 사용하지 않는 경우우

```sql
sqlite> SELECT time FROM shows, starts, people
        WHERE shows.id = stars.show_id
        AND people.id = stars.person_id
        AND name = 'Steve Carell';
```

- 2.76초 걸림
- `shows.id = stars.show_id`
  - shows.id: primary key (indexed by default)
  - stars.show_id: Foreign key (not indexed by default)
- 외래키에 인덱스가 없기 때문에 Join 연산이 비효율적임(테이블의 모든 행을 검사하면서 shows.id와 비교해야하는 경우 느려짐)

  > 동작 방식
  >
  > - shows 테이블에서 Index 연산으로 id 값 가져옴(O(1))
  > - stars 테이블에서 show_id = shows.id인 레코드 찾음, 인덱스가 없기 때문에 전체 검색 발생 가능(O(N))
  > - people 테이블에서 name 'Steve Carell'인 id를 찾음, 인덱스 없기 때문에 전체 검색 발생 가능(O(N))

### 조회할 테이블의 필드를 INDEX로 지정

```sql
CREATE INDEX 인덱스명 ON 테이블 (필드명);
```

```sql
sqlite> CREATE INDEX person_index ON stars (person_id);
sqlite> CREATE INDEX show_index ON stars (show_id);
sqlite> CREATE INDEX name_index ON stars (name_id);
```

- 위에서 조회한 모든 column를 INDEX로 지정

```sql
sqlite> SELECT time FROM shows, starts, people
        WHERE shows.id = stars.show_id
        AND people.id = stars.person_id
        AND name = 'Steve Carell';
```

- 0.001 초 걸림

# Python and SQL

```python
from cs50 import SQL

db = SQL("sqlite:///favorites.db")  # python 에서 DB 여는 법
favorite = input("Favorite: ")
rows = db.execute("SELECT COUNT(*) AS n FROM favorites WHERE problem=?", favorite)
row = rows[0]

print(row["n"])
```

### 동작 원리

1. 파일 열기
   - sqlite:/// → 현재 디렉토리에 있는 SQLite 파일을 사용하겠다는 의미.
   - favorites.db → 데이터베이스 파일 이름.
2. 쿼리 작성
   - ? = printf의 %s와 비슷하다고 생각하면 됨, 현재 코드에서는 ?에 favorite이 할당됨
3. row = rows[0]
   - db.execute는 결과를 리스트 형태로 반환하기 때문에 (`rows = [{"n": 5}]`) 첫 번째를 가져와야 원하는 결과를 가져올 수 있음
4. COUTN(\*) 값을 가져와 출력

```sql
sqlite3> SELECT COUNT(*) AS n FROM favorites WHERE problem="Movie"
```

- 위와 같이 활용용

# Race Conditions

```python
rows = db.execute("SELECT likes FROM posts WHERE id = ?", id)
likes = rows[0]['likes']
db.execute("Update posts SET likes = ? WHERE id = ?", likes + 1, id)
```

- 좋아요를 눌렀을 때 좋아요 수가 업데이트 되는 코드
- 여러 유저가 한 번에 좋아요를 누른다면? > DB에 업데이트 될 내용(이미지)이 한 번에 연산되어야 하는 상황이 옴
- 연산이 겹치는 경우 누락되는 연산이 생길 수 있음

## 해결 방법

### BEGIN TRANSACTION - COMMIT

```python
db.execute("BEGIN TRANSACTION")
rows = db.execute("SELECT likes FROM posts WHERE id = ?", id)
likes = rows[0]['likes']
db.execute("UPDATE posts SET likes = ? WHERE id = ?", likes + 1, id)
db.execute("COMMIT")
```

- db.execute("BEGIN TRANSACTION")과 COMMIT 사이의 세 줄은 한 번에 실행되거나, 아예 실행되지 않음(ex - 세 줄 중 두 줄이 실행되고 마지막에 오류 나서 안된다 -> 실행되었던 위의 두 줄도 실행 안된 상태로 돌아감(원자성 유지))

> 원자성 유지: 트랜잭션 내의 모든 작업이 모두 실행되거나, 하나도 실행되지 않음

# SQL Injection

## 예시

- `ssafy@gmail.com'--`로 로그인을 한다고 해보자.(기존 아이디에 `'--`를 붙인 것)

- DB 상에서 다음과 같은 방식으로 로그인 데이터를 처리한다고 한다면 발생할 수 있는 문제점은?
  ```python
  rows = db.execute(f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'")
  ```
- 다음과 같은 문제가 발생할 수 있음

  ```python
  rows = db.execute(f"SELECT * FROM users WHERE username = 'ssafy@gmail.com'--' AND password = '{password}'")
  ```

  - --' 이후로는 [인식을 하지 못함](#예시) (--가 SQLite 상 주석으로 인식되기 때문)= password가 없어도 username만 알면 로그인이 되는 것

- 해결 방법: escape 문자 (') 사용
  ```python
  rows = db.execute(f"SELECT * FROM users WHERE username = 'ssafy@gmail.com''--' AND password = '{password}'")
  ```
- Parameterized Query 사용
  ```python
  rows = db.execute("SELECT * FROM users WHERE username = ? AND password = ?", username, password)
  ```

# 끝!

![alt text](./Yeyeong_images/image-3.png)
