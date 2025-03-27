# CS50 Lecture 7 - SQL - Querying
<br>

  ```sql
    sqlite3 shows.db
  ```

![image](https://raw.githubusercontent.com/Y00CHAN/Images/refs/heads/master/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202025-03-27%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%2011.01.19.png)

> ### SELECT

- **기본 구조**
  - `SELECT` 문은 데이터베이스에서 원하는 데이터를 조회할 때 사용 <br>`SELECT 열_이름 FROM 테이블_이름;`

- **모든 열 조회** 
  - 모든 열을 조회할 때 <br>`SELECT * FROM 테이블_이름;`
  ```sql
    SELECT * FROM shows;
  ```

- **조건부 조회**
  - 조건에 맞는 행만 조회<br> `SELECT * FROM 테이블_이름 WHERE 조건;`

  ```sql
    SELECT show_id FROM ratings WHERE rating >= 6.0 LIMIT 10;
  ```

    - LIMIT : 갯수 제한 (원래는 무작위로 주어진 갯수만큼 가져옴)

      - 참고

        LIMIT만 쓰면 DBMS(Database Management System)는 내부적으로 "정렬 기준 없음" 상태로 10개를 잘라서 주는데,

        DB 엔진이 항상 같은 순서로 데이터를 스캔하면 결과도 같을 수 있다 (예: MySQL의 경우 인덱스 순서에 따를 수도 있음)

        하지만, 이 순서가 보장된 건 아님

        ORDER BY가 없으면, 어떤 기준으로 잘라내는지는 명시적이지 않아서 예측이 안 되는 게 원칙이다. 그러니까 DB가 운 좋게 같은 결과를 주는 것처럼 보이지만, 나중에 테이블이 변경되거나 엔진이 바뀌면 결과가 바뀔 수도 있다


> ### Subquery

- 쿼리 안에 또 다른 쿼리를 삽입해서 복잡한 조건을 처리

  ```sql
  SELECT title FROM shows WHERE id IN (SELECT show_id FROM ratings WHERE rating >= 6.0);
  ```
    직독직해 : shows 중에서 title 을 선택해라 / id 가 (ratings 안에있는 rating이 6.0 이상인 show_id) 안에 있으면.
---

> ### JOIN

- 여러 테이블을 공통 열을 기준으로 결합해서 조회

  ```sql
  SELECT * FROM shows JOIN ratings ON shows.id = ratings.show_id WHERE rating >= 6.0 LIMIT 10;
  ```
  ```sql
  SELECT title, rating FROM shows JOIN ratings ON shows.id = ratings.show_id WHERE rating >= 6.0 LIMIT 10;
  ```

> ### One to Many

- 숫자열을 알고있다면 그걸로 검색하면 됨 


  ```sql
  SELECT genre FROM genres WHERE show_id = 63881;
  ```
- 근데 그건 무식한 짓. 검색을 하자
  ```sql
  SELECT id FROM shows WHERE title = 'Catweazle';
  ```
- 그리고 그걸 조건에 넣어서 원하는 걸 찾아내자
  ```sql
  SELECT genre FROM genres WHERE show_id = (SELECT id FROM shows WHERE title = 'Catweazle');
  ```
<br>

>### Many to Many
<br>

- 시리즈물. 방영한 연도가 너무 많다

  ```sql
  SELECT * FROM shows WHERE title = 'The Office';
  ```
- 정보를 좁혀나가서 이 id를 기억해서 쓰면 무식한 짓.

  ```sql
  SELECT id FROM shows WHERE title = 'The Office' AND year = 2005;
  ```
- 조건에 넣어서 원하는 정보를 향해 나아가자
  ```sql
  SELECT person_id FROM stars WHERE show_id = (SELECT id FROM shows WHERE title = 'The Office' AND year = 2005);
  ```
- 마지막으로 진짜 얻고싶은 2005년도 방영된 The Office의 출연진

  ```sql
  SELECT name FROM people WHERE id IN
  (SELECT person_id FROM stars WHERE show_id = (SELECT id FROM shows WHERE title = 'The Office' AND year = 2005));
  ```
