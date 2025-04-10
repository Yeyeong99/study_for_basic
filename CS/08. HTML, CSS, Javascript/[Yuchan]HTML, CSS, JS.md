t
# CS50 Lecture 8 - HTML, CSS, JavaScript

> ###  Bootstrap

- 반응형 웹사이트를 쉽게 개발할 수 있도록 도와주는 CSS 프레임워크
- 미리 정의된 클래스들을 이용해 빠르게 UI를 구성할 수 있음

[Bootstrap Link](https://getbootstrap.com/)

> ###  JavaScript

- 웹 페이지에 동적 기능을 부여하는 프로그래밍 언어
- 상호작용적이고 반응성이 뛰어남

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <script>
      // 페이지의 HTML 문서가 완전히 로드된 후 실행됨
      document.addEventListener('DOMContentLoaded', function() {
        // form 요소가 submit 되었을 때 실행할 이벤트 핸들러 등록
        document.querySelector('form').addEventListener('submit', function(event) {
          // id가 'name'인 input 요소에서 입력된 값을 가져와 alert로 출력
          alert('hello, ' + document.querySelector('#name').value);  
          // 폼의 기본 제출 동작(페이지 새로고침 등)을 막음
          event.preventDefault();
        });
      });
    </script>  

    <title>hello</title>
  </head>

  <body>
    <!-- 사용자 입력을 받을 form -->
    <form>
      <!-- 자동완성 off, 포커스 자동 지정, id와 name이 'name'인 텍스트 입력 필드 -->
      <input autocomplete="off" autofocus id="name" name="name" placeholder="Name" type="text">
      <!-- 제출 버튼 -->
      <input type="submit">
    </form>
  </body>
</html>

```

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <!-- 파일로 대체 -->
    <script src="scripts.js"></script>
    <title>hello</title>
  </head>
  <body>
    <form>
      <input autocomplete="off" autofocus id="name" name="name" placeholder="Name" type="text">
      <input type="submit">
    </form>
  </body>
</html>

```


> ### Background

- JavaScript를 이용하여 웹 페이지 내부에서 CSS를 수정하는 예제

```html
<body>
  <!-- 각각 빨강, 초록, 파랑 배경색을 설정할 버튼 3개 -->
  <button id="red">R</button>
  <button id="green">G</button>
  <button id="blue">B</button>

  <script>
    // body 요소를 선택하여 변수에 저장
    let body = document.querySelector('body');

    // 빨간 버튼 클릭 시 배경색을 빨강으로 변경
    document.querySelector('#red').addEventListener('click', function () {
      body.style.backgroundColor = 'red';
    });

    // 초록 버튼 클릭 시 배경색을 초록으로 변경
    document.querySelector('#green').addEventListener('click', function () {
      body.style.backgroundColor = 'green';
    });

    // 파란 버튼 클릭 시 배경색을 파랑으로 변경
    document.querySelector('#blue').addEventListener('click', function () {

      // CSS처럼 background-color 쓰면 안됩니까?
      // 안된다. 왜? JS는 수학을 알기때문에 '-' 연산자로 인식하기 때문 
      body.style.backgroundColor = 'blue';
    });
  </script>
</body>

```


> ### Blink

- 깜빡깜빡 실습

```html
  <script>
    // greeting의 표시 여부를 토글하는 함수
    function blink() {
      // body 요소를 선택해서 변수에 저장
      let body = document.querySelector('body');

      // 현재 body의 visibility가 'hidden'이면
      if (body.style.visibility == 'hidden') {
        // 보이도록 바꿈
        body.style.visibility = 'visible';
      } else {
        // 아니면 숨김
        body.style.visibility = 'hidden';
      }
    }

    window.setInterval(blink, 500);
  </script>
```


> ### Autocomplete

```html
<form>
  <input type="text" name="name" autocomplete="on" placeholder="이름을 입력하세요">
  <input type="submit">
</form>
```

- `autocomplete="off"`로 설정하면 자동 완성 비활성화

---

> ### Summary

- HTML로 웹페이지를 구성 하고
- CSS로 스타일 꾸미고
- JavaScript로 웹페이지를 동적으로 업데이트하고 수정하자!
