# 2/15(수)

## Stack(이전 수업에서 계속)

* 중위 표기법(Infix notation) : 연산자를 피연산자의 가운데에 표기하는 방법 (A + B)
* 후위 표기법(Postfix notation) : 연산자를 피연산자 뒤에 표기하는 방법 (AB+)

### 계산기 - 중위 표기법(스택 이용)

1. 입력 받은 중위 표기식에서 토큰을 읽는다.
2. 토큰이 피연산자(숫자 등)라면 토큰을 출력한다.
3. 토큰이 연산자(괄호 포함)라면
   1. 이 토큰이 스택의 top에 저장된 연산자보다 우선순위가 높으면 push
   2. 그렇지 않다면 스택 top 연산자의 우선순위가 토큰의 우선순위보다 작을 때까지 스택에서 pop한 후 토큰의 연산자 push
   3. top에 연산자가 없으면 push
4. 토큰이 오른쪽 괄호 ')'라면 스택 top에 왼쪽 괄호 '('가 나올때까지 스택에 pop 계속 수행하고 pop한 연산자를 출력한다. 왼쪽 괄호를 만나면 pop만 하고 출력 X
5. 중위 표기식에 더 읽을 것이 없다면 중지하고, 더 읽을 것이 있다면 처음부터 다시 반복
6. 스택에 남아 있는 연산자를 모두 pop하여 출력한다.



### 계산기 - 후위 표기법

* 앞서 중위 표기법에서 후위 표기법으로 수식을 바꾼 상태에서 수식 계산

1. 피연산자(숫자 등)를 만나면 스택에 push
2. 연산자를 만나면 필요한 만큼의 피연산자를 스택에서 pop, 이 후 연산 결과를 다시 스택에 push
3. 수식이 끝나면 마지막으로 스택을 pop하여 출력



### 백트래킹(Backtracking)

* 해를 찾는 도중에 '막히면' (해가 아니면) 되돌아가서 다시 해를 찾아가는 기법
* 최적화(Optimization) 문제와 결정(Decision) 문제 해결 가능
* 결정 문제 : 문제의 조건을 만족하는 해가 존재하는지의 여부를 'yes' 또는 'no'로 답하는 문제
  * 미로찾기, n-Queen 문제, Map coloring, 부분 집합의 합(Subset Sum) 문제 등

* 백트래킹 vs DFS

  * 어떤 노드에서 출발하는 경로가 해결책으로 이어질 것 같지 않으면 더 이상 그 경로를 따라가지 않음으로써 시도 횟수를 줄임 (Prunning(가지치기))

  * 깊이우선탐색은 모든 경로를 추적, 백트래킹은 불필요한 경로를 조기 차단

  * 깊이우선탐색은 경우의 수가 너무 많음

  * 백트래킹을 적용하면 일반적으로 경우의 수가 줄어들지만 이 역시 최악의 경우에는 여전히 지수함수 시간 (Exponential Time)을 요함

* 백트래킹 절차

  1. 상태 공간 트리의 깊이 우선 검색 실시
  2. 각 노드가 유망한지 점검
  3. 그 노드가 유망하지 않다면 그 노드의 부모 노드로 돌아가서 검색 계속 진행

#### 부분집합 구하기

* 부분집합(Powerset) : 어떤 집합의 공집합과 자기 자신을 포함한 모든 부분집합

  * 어떤 집합의 원소 개수가 n개라면 부분집합의 개수는 2^n개

* 백트래킹 활용해보기

  * 2^n개의 부분집합을 만들 때

* 부분집합 생성하기

  ```python
  bit = [0, 0, 0, 0]
  for i in range(2):
      bit[0] = i					# 0번째 원소
      for j in range(2):
          bit[1] = j				# 1번째 원소
          for k in range(2):
              bit[2] = k			# 2번째 원소
              for l in range(2):
                  bit[3] = l		# 3번째 원소
                  print(bit)		# 생성된 부분집합 출력
  ```

* powerset을 구하는 백트래킹 알고리즘

  ```python
  def backtrack(a, k, input):  # 백트래킹 함수
      global MAXCANDIDATES
      c = [0] * MAXCANDIDATES
      
      if k == input:
          process_solution(a, k)  # 답이면 원하는 작업 진행
      else:
          k += 1
          ncandidates = construct_candidates(a, k, input, c)
          for i in range(ncandidates):
              a[k] = c[i]
              backtrack(a, k, input)
              
  def construct_candidates(a, k, input, c):  # 부분집합 생성 함수
      c[0] = True
      c[1] = False
      return 2
  
  MAXCANDIDATES = 3
  NMAX = 4
  a = [0] * NMAX
  backtrack(a, 0, 3)
  ```

#### 순열 구하기

````python
def backtrack(a, k, input):  # 백트래킹 함수
    global MAXCANDIDATES
    c = [0] * MAXCANDIDATES
    
    if k == input:
        for i in range(1, k+1):
            print(a[i], end=" ")
        print()
    else:
        k += 1
        ncandidates = construct_candidates(a, k, input, c)
        for i in range(ncandidates):
            a[k] = c[i]
            backtrack(a, k, input)
            
def construct_candidates(a, k, input, c):  # 순열 생성 함수
    in_perm = [False] * NMAX
    
    for i in range(1, k):
        in_perm[a[i]] = True
        
    ncandidates = 0
    for i in range(1, input + 1):
        if in_perm[i] == False:
            c[ncandidates] = i
            ncandidates += 1
    return ncandidates

MAXCANDIDATES = 3
NMAX = 4
a = [0] * NMAX
backtrack(a, 0, 3)

```
1 2 3 
1 3 2 
2 1 3 
2 3 1 
3 1 2 
3 2 1 
```
````

