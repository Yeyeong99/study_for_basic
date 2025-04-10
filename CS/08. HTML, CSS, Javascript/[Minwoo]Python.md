### Harvard Pep Squad Prank
![alt text](<minwoo_아저씨 이건 왜 보여주시나요.jpg>)


#### ? 




---

## 🎭 Harvard vs Yale 장난 영상
- Yale 학생들이 Harvard를 상대로 한 전설적인 장난 영상 시청
- 하버드 응원단에 Yale이 만든 피켓을 몰래 배포 → “WE SUCK” 메시지가 공개됨
- 유쾌한 라이벌 구도 소개 후 본격 수업 시작

---
### Regular Expressions
## 📄 HTML + Regex (정규표현식) + 클라이언트 검증


## 🧠 요약

- HTML로 구조를, CSS로 디자인을, Regex로 패턴을!
- 정규표현식은 이메일, 전화번호, 비밀번호 등 사용자 입력 검증에 매우 유용
- **검증은 반드시 서버에서도 한 번 더 해야 함**
- 개발자 도구를 활용해 **학습**도, **디버깅**도, **보안 테스트**도 가능



### 🔤 HTML `<form>` 구성 예제

```html
<form>
  <input 
    type="email" 
    name="email" 
    placeholder="email" 
    autocomplete="off" 
    autofocus 
    pattern=".+@.+\.edu" 
  />
  <button>Register</button>
</form>
```

- `type="email"` → 브라우저가 기본적인 이메일 형식 검증함 (`@` 누락 시 오류)
- `pattern=".+@.+\.edu"` → **정규표현식**으로 `.edu` 도메인만 허용

---

### 🔍 정규표현식 (Regular Expressions, Regex)

#### ✨ 기호 뜻 요약

| 기호 | 의미 |
|------|------|
| `.` | 모든 문자 1개 |
| `+` | 1회 이상 반복 |
| `*` | 0회 이상 반복 |
| `?` | 0 또는 1회 |
| `{n}` | 정확히 n번 |
| `{n,m}` | 최소 n번, 최대 m번 |
| `[abc]` | a, b, c 중 하나 |
| `[0-9]` | 숫자 하나 |
| `\d` | 숫자 (0~9) |
| `\D` | 숫자가 아닌 문자 |
| `\.` | 진짜 마침표 (`.`를 특수문자 말고 그냥 점으로 인식) |

#### ✅ 예: `.+@.+\.edu`

- `.+` → 아무 문자 1개 이상  
- `@` → 문자 그대로의 @  
- `\.` → 마침표 문자  
- `edu` → edu로 끝나야 통과

---

### ❌ 클라이언트 검증의 한계

- 브라우저에서 검증한다고 **보안이 확보되는 건 아님!**
- 사용자가 개발자 도구로 HTML 코드를 바꾸면 패턴을 삭제할 수 있음
  → `.com`도 통과 가능
- **교훈**: 클라이언트(브라우저) 검증은 **친절용**이지, **보안용**은 아님!

---

## 🧑‍💻 개발자 도구(DevTools)

- 브라우저에서 HTML, CSS, JS 직접 수정 가능 (로컬에 한함)
- 악의적인 사용자는 이를 이용해 클라이언트 검증을 우회 가능
- 따라서 **서버 측 검증(백엔드)**이 반드시 필요

---

## ✅ HTML 문법 검사기

- [https://validator.w3.org/](https://validator.w3.org/)
- 작성한 HTML 코드를 붙여 넣으면 문법 오류를 알려줌
- 실무에서도 자주 사용함 (무료, 공식 도구)

---






### CSS(Cascading Style Sheets)
---

### ✅ **1. CSS의 기본 개념**
- **CSS는 key-value 쌍**으로 구성되어 있으며, 이를 *속성(properties)* 이라고 부름.
- HTML에서는 `key="value"` 형식이지만, CSS에서는 `key: value;` 형식 사용.
- 스타일은 HTML의 `style` 속성으로 직접 지정하거나 `<style>` 태그 혹은 별도 `.css` 파일로 분리 가능.

---

### ✅ **2. 스타일 적용 방식**
1. **Inline Style (인라인 스타일)**  
   HTML 태그 내에 `style` 속성을 직접 작성  
   예: `<p style="font-size: large; text-align: center;">`

2. **Internal Style (내부 스타일)**  
   `<head>` 내부에 `<style>` 태그로 작성  
   ```html
   <style>
     p {
       font-size: large;
     }
   </style>
   ```

3. **External Style (외부 스타일)**  
   별도의 `.css` 파일로 스타일을 작성하고 `<link>` 태그로 연결  
   ```html
   <link rel="stylesheet" href="style.css">
   ```

---

### ✅ **3. CSS 선택자 (Selectors)**
- `p`, `body`, `div`, `header`, `main`, `footer` 등 HTML 태그명 직접 사용 가능
- `.className`: 클래스 선택자 (여러 요소에 재사용 가능)
- `#idName`: 아이디 선택자 (단일 요소에 사용)

---

### ✅ **4. 스타일 재사용: 클래스 활용**
```css
.centered {
  text-align: center;
}
.large {
  font-size: large;
}
```
HTML에서:
```html
<p class="centered large">Hello!</p>
```

---

### ✅ **5. 시맨틱 태그의 중요성**
- `div` 대신 `header`, `main`, `footer` 등 **시맨틱 태그**를 사용하면  
  접근성(Accessibility), SEO, 유지보수에 더 유리함.

---

### ✅ **6. 스타일을 한 곳에 집중시키기**
- 스타일을 요소마다 개별 적용하지 않고 부모 태그에 적용하면 **"cascading"** 효과로 자식에게 전파됨.
- 중복 스타일을 줄이고 유지보수 용이.

---

### ✅ **7. HTML Entity 사용**
- 특수 기호는 `&copy;`, `&#169;` 등 HTML 엔티티를 통해 사용 가능  
  예: `&copy; John Harvard`

---

### ✅ **8. 외부 CSS 파일로 분리**
- 스타일 코드를 `.css` 파일로 분리하면 **협업**이나 **유지보수**에 유리  
  ex) `home.css`로 따로 저장하고 `<link>`로 연결

---

### ✅ **9. 링크 스타일링**
- `<a>` 태그도 CSS로 색상, 밑줄 등 스타일링 가능  
  ```css
  a {
    color: crimson;
    text-decoration: none;
  }

  a:hover {
    text-decoration: underline;
  }
  ```

####