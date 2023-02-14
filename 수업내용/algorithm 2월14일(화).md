# 2/14(화)

## 스택(이전 수업에서 계속)

### 재귀호출

* 자기 자신을 호출하여 순환 수행되는 것

* 함수에서 실행해야 하는 작업의 특성에 따라 일반적인 호출방식보다 재귀호출방식을 사용하여 함수를 만들면 프로그램의 크기를 줄이고 간단하게 작성

  ex) factorial

  * n에 대한 factorial : 1부터 n까지의 모든 자연수를 곱하여 구하는 연산

    ```
    n! = n * (n - 1)!
    	(n - 1)! = (n - 1) * (n - 2)!
    	(n - 2)! = (n - 2) * (n - 3)!
    ...
    	2! = 2 * 1!
    	1! = 1
    ```

  * 마지막에 구한 하위 값을 이용하여 상위 값을 구하는 작업 반복

  ex) 피보나치 수열

  * 0과 1로 시작하고 이전의 두 수 합을 다음 항으로 하는 수열

    * 0, 1, 1, 2, 3, 5, 8, 13, ...

  * 피보나치 수열의 i번째 값을 계산하는 함수 F

    F0 = 0, F1 = 1

    Fi = F(i-1) + F(i-2)  for i >= 2

    ```python
    def fibo(n):
        if n < 2:
            return n
        else:
            return fibo(n - 1) + fibo(n - 2)
    ```



### Memoization

* 피보나치 수열 재귀함수 → 엄청난 중복 호출 존재

* Memoization : 컴퓨터 프로그램 실행 시 이전에 계산한 값을 메모리에 저장하여 매번 다시 계산하지 않도록 하여 전체적인 실행속도를 빠르게 하는 기술

* 동적 계획법의 핵심 기술

* 피보나치 수를 구하는 알고리즘에서 fibo(n)의 값을 계산하자마자 저장하면(memoize), 실행시간을 Θ(n)으로 줄일 수 있다.

* Memoization 방법을 적용한 피보나치 수열 알고리즘

  ```python
  # memo를 위한 배열을 할당하고, 모두 0으로 초기화한다.
  # memo[0]을 0으로, memo[1]은 1로 초기화한다.
  
  def fibo1(n):
      global memo
      if n >= 2 and memo[n] == 0:
          memo[n] = (fibo1(n - 1) + fibo1(n - 2))
      return memo[n]
  
  memo = [0] * (n + 1)
  memo[0] = 0
  memo[1] = 1
  ```



### 동적 계획(DP, Dynamic Programming)

* 입력 크기가 작은 부분 문제들을 모두 해결 한 후, 그 해들을 이용하여 보다 큰 크기의 부분 문제들을 해결하여 최종적으로 원래 주어진 입력의 문제를 해결하는 알고리즘

* 그리디 알고리즘과 같이 최적화 문제를 해결하는 알고리즘

* DP 적용방법(피보나치 수열 예시)

  1. 문제를 부분 문제로 분할
     * fibo(n) = fibo(n - 1) - fibo(n - 2)
     * fibo(n - 1) = fibo(n - 2) + fibo(n - 3)
     * fibo(2) = fibo(1) + fibo(0)
     * fibo(n)은 fibo(n - 1), fibo(n - 2), ... , fibo(2), fibo(1), fibo(0)의 부분집합으로 나뉜다.
  2. 가장 작은 부분 문제부터 해를 구한다.
  3. 그 결과를 테이블에 저장하고, 테이블에 저장된 부분 문제의 해를 이용하여 상위 문제 해를 구한다.

* DP 적용 피보나치 수열 알고리즘

  ```python
  def fibo2(n):
      f = [0] * (n + 1)
      f[0] = 0
      f[1] = 1
      for i in range(2, n + 1):
          f[i] = f[i -1] + f[i - 2]
          
      return f[n]
  ```

* DP 구현 방식

  * recursive 방식 : fib1()
  * iterative 방식 : fib2()

* memoization을 재귀적 구조에 사용하는 것보다 반복적 구조로 DP를 구현하는 것이 성능 면에서 보다 효율적

* 재귀적 구조 → 내부에 시스템 호출 스택을 사용하는 오버헤드 발생



### DFS(깊이우선탐색)

* 비선형구조인 그래프 구조는 그래프로 표현된 모든 자료를 빠짐없이 검색하는 것이 중요함

* 두 가지 방법

  * 깊이 우선 탐색(Depth First Search, DFS)
  * 너비 우선 탐색(Breadth First Search, BFS)

* DFS : 시작 정점의 한 방향으로 갈 수 있는 경로가 있는 곳까지 깊이 탐색해 가다가 더 이상 갈 곳이 없게 되면 가장 마지막에 만났던 갈림길 간선이 있는 정점으로 되돌아와서 다른 방향의 정점으로 탐색을 계속 반복하여 결국 모든 정점을 방문하는 순회방법

* 가장 마지막에 만났던 갈림길의 정점으로 되돌아가서 다시 깊이 우선 탐색을 반복해야함

  → 후입선출 구조의 스택 사용

#### DFS 알고리즘

1. 시작 정점 v를 결정하여 방문
2. 정점 v에 인접한 정점 중에서
   1. 방문하지 않은 정점 w가 있다면 정점 v를 스택에 push하고 정점 w 방문, 그리고 w를 v로 하여 다시 반복
   2. 방문하지 않은 정점이 없으면, 탐색의 방향을 바꾸기 위해 스택을 pop하여 받은 가장 마지막 방문 정점을 v로 하여 다시 반복
3. 스택이 공백이 될 때까지 2. 반복

```python
visited = []
stack = []
DFS(v)
	# 시작점 v 방문
    visited[v] = True:
    while
    	if ( v 인접 정점 중 방문 안 한 정점 w가 있다면):
            push(v):
                v = w
                visited[w] = True
        else:
            if len(stack) != 0:
                stack.pop(v)
            else:
                break
```



* 저장 방법

  ```python
  '''
  7 8
  1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
  '''
  
  V, E = map(int, input().split())
  arr = list(map(int, input().split()))
  adjM = [[0] * (V + 1) for _ in range(V + 1)]
  adjL = [[] for _ in range(V + 1)]
  
  for i in range(E):
      v1, v2 = arr[i * 2], arr[i * 2 + 1]
      adjM[v1][v2] = 1
      adjM[v2][v1] = 1
      
      adjL[v1].append(v2)
      adjL[v2].append(v1)
  ```

  

