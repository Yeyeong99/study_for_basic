# study_4_git

## 세부 사항

### 일정 | 2025.01.31 - 2025.04.09

### Repository 구조

```Markdown
study_4_git
    ㄴ CS
        ㄴ C
            ㄴ [Nayeon]C.md
            ㄴ [Dahye]C.md
            ㄴ [Yoochan]C.md
            ㄴ [Yeyeong]C.md
        ㄴ Arrays
        ㄴ Algorithm
        ㄴ ...

    ㄴ algorithm
        ㄴ Nayeon
        ㄴ Dahye
        ㄴ Yoochan
        ㄴ Yeyeong
```

## 스터디 목적

1. Git 사용법 익히기
2. CS50 강의 훑어보기
3. 알고리즘 풀이 습관화

## CS 스터디 (대면)

[참고자료](https://www.youtube.com/watch?v=cwtpLIWylAw&list=PLhQjrBD2T381WAHyx1pq-sBfykqMBI7V4)

1. 시간: 매주 금요일 점심시간 모임
2. 일주일에 개념 한 개씩

- 각자 맡을 부분을 분배, 공부한 자료 md 파일로 각 주제에 맞는 레포지토리에 올리기
  - [이름(영어로)]CS*개념*이름.md
  - 파일 업로드는 발표 전 일요일 11:59:59까지

## 알고리즘 스터디 (비대면)
>  **pull request 과정에서 다른 사람 코드 리뷰하고 댓글 남기기**

[참고자료](https://swexpertacademy.com/main/main.do)

1. 매일 주어지는 SWEA 과제 풀이를 목표로 함 
2. 풀이 공유 방법
   - 요약: local에서 branch 생성 후 새 branch에서 작업, push, 깃허브 웹 사이트에서 pull-request 수행
   - main 브랜치는 웹 깃허브 상에서만 조작한다고 생각하면 됨
   - 로컬에서는 자신의 이름을 한 브랜치에서만 작업할 것
   - 1회차 / 1주차 스터디 전: 제일 처음 clone하고 브랜치를 로컬에서 생성해 push할 때
     |번호|명령어|설명|
     |:-:|:-:|:-|
     |1|git clone 주소|처음에만 하면 됨|
     |2|git branch Yeyeong|Yeyeong이라는 이름의 브랜치 생성. 자신의 이름으로 하면 됨|
     |3|git checkout Yeyeong|Yeyeong이라는 이름의 브랜치로 이동, checkout 대신 switch 써도 됨|
     |4| |로컬에서 작업 진행|
     |5|git add 파일이름|파일 이름 혹은 . 이용|
     |6|git commit -m "커밋 메세지"|커밋 시 원하는 issue의 넘버를 쓰면 링크가 연동됨. 예를 들어 #2를 쓰면 #2 issue로 연결되는 식|
     |7|git push|레포지토리에 올림|
     |8||git hub 웹사이트에 잘 올라갔는지 확인|

     
   - 1회차 / 1주차 스터디 이후: 레포지토리를 받아오고 한 번 푸시를 한 이후
     |번호|명령어|설명|
     |:-:|:-:|:-|
     |1|git checkout Yeyeong|Yeyeong이라는 이름의 브랜치로 이동, checkout 대신 switch 써도 됨|
     |2|**git pull origin Yeyeong**|1) **자신의 브랜치에 있는 상태에서**<br>2) 웹 깃허브 상에서 자신의 브랜치에서 업데이트 된 내용을 받아오기 위한 과정<br>3) **안하면 충돌 가능성 높아지니 필수!!**|
     |3| |로컬에서 작업 진행|
     |4|git status|작업 상태 확인|
     |5|git add 파일이름|파일 혹은 . 이용|
     |6|git commit -m "커밋 메세지"|커밋 시 원하는 issue의 넘버를 쓰면 링크가 연동됨. 예를 들어 #2를 쓰면 #2 issue로 연결되는 식|
     |7|git push|레포지토리에 올림|
     |8||git hub 웹사이트에 잘 올라갔는지 확인|
        - 현재 자신이 위치한 브랜치 확인하는 방법: git branch 치거나 git bash의 레포지토리 맨 뒤에 괄호 안 이름 확인
        - 만약 git branch 잘못 만들었을 경우: git branch -d 브랜치 이름 하면 됨
