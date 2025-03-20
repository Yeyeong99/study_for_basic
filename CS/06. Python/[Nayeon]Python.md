# 📝 Python 주요 개발 정보  

## 🔹 Functions (함수)  

### ✅ Python과 C의 차이  
- C는 **타입을 지정**해야 하지만, Python은 **자동 형 변환** 수행.  
- C에서는 `scanf()`로 입력받지만, Python에서는 `input()`을 사용.  

### ⛔ `scanf()`를 사용하지 않는 이유  
1. **버퍼 오버플로우 발생 가능** (길이 제한이 없을 경우 위협)  
2. **Python은 자동 머먼트 할당**을 지원하여 더 안전함.  
3. **유연한 입력 처리 가능** (형식을 맞이면서 입력할 필요 없음).  

---

### ⚠️ **함수 사용 시 주의해야 할 점** 

```python
def add_item(item, items=[]):
    items.append(item)
    return items

print(add_item(1))  
print(add_item(2))  
```
📌 **Python에서 함수의 기본 인자는 함수가 정의될 때 한 번만 평가

```python
x = 10
def foo():
    x = 20
foo()
print(x)
```

```python
a = [1, 2, 3]
b = a
b.append(4)
print(a)
```

```python
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a == c)
print(a is c)  
```

## 🔹 Types (자동 형)  

### 🧐 `input()`에서 숫자를 입력해도 `str`로 저장되는 이유?  
📌 **Python의 `input()`은 특정한 형태를 결정하지 않고 무조건 `str`로 보유되도록 설계되어 있다.**  


# calculator
print(0.1 + 0.2)  # 0.30000000000000004 ❌

해결법?
from decimal import Decimal
print(Decimal("0.1") + Decimal("0.2"))  # 0.3

# conditionals

```python
if 0:
    print("참")  # 실행 안됨
if "":
    print("참")  # 실행 안됨
if None:
    print("참")  # 실행 안됨
```