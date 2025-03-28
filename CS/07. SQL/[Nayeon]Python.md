# CS50: SQL 수업 정리

## Relational Databases (관계형 데이터베이스)

### "엑셀보다 똑똑한 데이터 저장소"
- 관계형 데이터베이스는 데이터를 표(table) 형태로 저장하며, 서로 연결된 관계를 통해 더 유연하게 정보를 다룰 수 있다.

### 엑셀에 비유하자면?
| 🧮 스프레드시트(엑셀) | 🗃️ 관계형 데이터베이스 |
|--------------------|-------------------------|
| 시트 (sheet)        | 테이블 (table)           |
| 셀 (cell)           | 필드 (field)             |
| 행 (row)            | 레코드 (record)          |
| 열 (column)         | 컬럼 (column)            |
- 여러가지 시트를 서로 연결해 쓸 수 있다는 강점.

### SQL로 할 수 있는 핵심 작업 : CRUD
| 작업 (Operation) | SQL 명령어 (SQL Command) | 설명 (Description)              |
|------------------|---------------------------|----------------------------------|
| 🆕 Create         | `INSERT`                  | 새로운 데이터 추가 (Add new data) |
| 🔍 Read           | `SELECT`                  | 데이터 조회 (Retrieve data)      |
| ✏️ Update         | `UPDATE`                  | 기존 데이터 수정 (Modify data)   |
| ❌ Delete         | `DELETE`                  | 데이터 삭제 (Remove data)        |

- 즉, 단순히 데이터 저장하는 장소가 아닌, 내가 원하는 방식으로 다룰 수 있음.

### 타입 지정
```SQL
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER,
    email TEXT UNIQUE
)
```
- **INTEGER, TEXT, REAL(실수), BOOLEAN** 등 다양한 데이터 타입
- **PRIMARY KEY** : 고유 식별자(행 구별해주는 고유 값)
- **NOT NULL, UNIQUE**: 제약조건

## sqlite3
- SQL 데이터베이스 도구
- 아이폰, 안드로이드, 브라우저 등에 내장될 만큼 가볍고 유용.
- 가볍고 설치 없이 바로 사용 가능.

### SQLite 사용법 in CodeSpace

```SQL
& sqlite3 favorites.db
sqlite> .mode csv
sqlite> .import favorites.csv favorites
sqlite> .schema 
sqlite> SELECT * FROM favorites;
sqlite> .quit
```

### 자주 쓰이는 SQL 문법
| 기능 (Function)      | 문법 예시 (SQL Syntax)                              | 설명 (Description)                          |
|----------------------|------------------------------------------------------|----------------------------------------------|
| 전체 조회             | `SELECT * FROM table;`                               | 테이블의 모든 데이터를 조회                 |
| 조건 조회             | `SELECT * FROM table WHERE column = 'X';`            | 특정 조건에 해당하는 데이터 조회           |
| LIKE 검색            | `SELECT * FROM table WHERE name LIKE '%na%';`        | 특정 문자열이 포함된 데이터 검색           |
| 정렬                 | `SELECT * FROM table ORDER BY column ASC/DESC;`      | 특정 컬럼을 기준으로 오름/내림차순 정렬    |
| 갯수 세기            | `SELECT COUNT(*) FROM table;`                        | 전체 행(row)의 개수 계산                    |
| 중복 제거            | `SELECT DISTINCT column FROM table;`                 | 중복을 제거한 고유한 값만 조회             |
| 그룹화               | `SELECT column, COUNT(*) FROM table GROUP BY column;`| 특정 컬럼 값별로 그룹화 후 집계             |
| 제한                 | `SELECT * FROM table LIMIT 5;`                       | 상위 5개 결과만 조회                        |
| 삭제                 | `DELETE FROM table WHERE 조건;`                      | 조건에 맞는 데이터 삭제                    |
| 수정                 | `UPDATE table SET column = '값' WHERE 조건;`         | 조건에 맞는 데이터 수정                    |

<br>

### 🎬 실생활 예시 (무슨 명령인지 맞춰보세요~~)
```SQL
SELECT title, COUNT(*) 
FROM favorites 
WHERE title LIKE '%Harry%' 
GROUP BY title 
ORDER BY COUNT(*) DESC 
LIMIT 3;
```

### 중요 개념 요약
- **관계형 데이터베이스**는 여러 테이블을 서로 연결해 관리할 수 있는 구조

- **SQL**은 데이터를 생성(C), 읽기(R), 수정(U), 삭제(D)하는 언어

- **SQLite**는 SQL을 가볍게 실행할 수 있는 도구 (설치 필요 없음)

- **SELECT + WHERE + ORDER BY + GROUP BY + LIMIT** = 데이터 필터링 & 정렬 핵심