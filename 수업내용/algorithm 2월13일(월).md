# 2/13(월)

## Stack

### 스택의 특성

* 물건을 쌓아 올리듯 자료를 쌓아 올린 형태의 자료구조
* 스택에 저장된 자료는 선형 구조를 갖는다.
  * 선형구조 : 자료 간의 관계가 1대1의 관계를 갖는다.
  * 비선형구조 : 자료 간의 관계가 1대N의 관계를 갖는다. ( ex) 트리)
* 스택에 자료를 삽입하거나 스택에서 자료를 꺼낼 수 있다.
* 마지막에 삽입한 자료를 가장 먼저 꺼낸다 → 후입선출(LIFO, Last - In - First - Out)
  * 1, 2, 3 순으로 자료 삽입 후 꺼내면 역순으로 3, 2, 1 순으로 꺼냄



### 스택의 구현

* 자료구조 : 자료를 선형을 저장할 저장소
  * 배열 사용 가능
  * 저장소 자체를 스택이라고 부르기도 한다.
  * 스택에서 마지막 삽입된 원소의 위치 → top이라고 부른다.
* 연산
  * 삽입(push) : 저장소에 자료 저장
  * 삭제(pop) : 저장소에서 자료를 꺼냄, 꺼낸 자료는 삽입한 자료의 역순으로 꺼냄
  * isEmpty : 스택이 공백인지 아닌지 확인하는 연산
  * peek : 스택의 top에 있는 item(원소)을 반환하는 연산
* push 알고리즘

```python
def push(item):
    s.append(item)  # 느리다는 단점 존재
```

```python
def push(item, size):
    global top
    top += 1
    if top == size:
        print('overflow!')
    else:
        stack[top] = item
        
size = 10
stack = [0] * size
top = -1

push(10, size)
top += 1
stack[top] = 20
```

* pop 알고리즘

```python
def pop():
    if len(s) == 0:
        # underflow
        return
    else:
        return s.pop()
```

```python
def pop():
    global top
    if top == -1:
        print('underflow')
        return 0
    else:
        top -= 1
        return stack[top + 1]
    
print(pop())

if top > -1:   # pop()
    top -= 1
    print(stack[top + 1])
```

* 스택 구현 시 고려사항
  * 1차원 배열 사용하여 구현 시 용이하다는 장점이 있지만 스택 크기 변경이 어렵다는 단점이 있다.
  * 해결 방안으로 저장소를 동적으로 할당하여 스택을 구현하는 방법이 있다. → 동적 연결리스트 이용
    * 구현이 복잡하다는 단점이 있지만 메모리를 효율적으로 사용한다는 장점을 가진다.
  * (여기서는 안함)



### 스택 응용 - 괄호검사

* 괄호 종류 : 대괄호 ( [] ), 중괄호 ( {} ), 소괄호 ( () )
* 조건
  * 왼쪽 괄호 개수와 오른쪽 괄호 개수가 같아야 한다.
  * 같은 괄호에서 왼쪽 괄호는 오른쪽 괄호보다 먼저 나와야 한다.
  * 괄호 사이에는 포함관계만 존재한다.
* 알고리즘 개요
  * 문자열에 있는 괄호를 차례대로 조사하면서 왼쪽 괄호를 만나면 스택에 push, 오른쪽 괄호를 만나면 스택에서 top 괄호를 삭제한 후 오른쪽 괄호와 짝이 맞는지 검사
  * 이 때 스택이 비어 있으면 조건1 또는 조건2에 위배
  * 괄호 짝이 맞지 않으면 조건3에 위배
  * 마지막 괄호까지 조사한 후에도 스택에 괄호가 남아 있으면 조건1에 위배



### 스택 응용 - function call

* 프로그램에서의 함수 호출과 복귀에 따른 수행 순서 관리
  * 가장 마지막에 호출된 함수가 가장 먼저 실행을 완료하고 복귀하는 LIFO 구조
  * 함수 호출 발생 시 호출한 함수 수행에 필요한 지역변수, 매개변수 및 수행 후 복귀할 주소 등의 정보를 스택 프레임(stack frame)에 저장하여 시스템 스택에 삽입
  * 함수 실행이 끝나면 시스템 스택의 top 원소(스택 프레임)를 삭제(pop)하면서 프레임에 저장되어 있던 복귀 주소를 확인하고 복귀
  * 함수 호출과 복귀에 따라 이 과정을 반복하여 전체 프로그램 수행이 종료되면 시스템 스택은 공백 스택이 된다.

