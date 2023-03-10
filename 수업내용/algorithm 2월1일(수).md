# 2/1(화)

## 알고리즘

* 유한한 단계를 통해 문제를 해결하기 위한 절차나 방법
* 컴퓨터가 어떤 일을 수행하기 위한 단계적 방법
* 어떠한 문제를 해결하기 위한 절차
* 알고리즘 표현 방법
  * 의사코드(슈도코드 , Pseudocode)
  * 순서도
* APS 과정의 목표 중 하나 : 보다 좋은 알고리즘을 이해하고 활용하는 것
* 좋은 알고리즘이란?
  * 정확성 : 얼마나 정확하게 동작하는가?
  * 작업량 : 얼마나 적은 연산으로 원하는 결과를 얻어내는가
  * 메모리 사용량 : 얼마나 적은 메모리를 사용하는가
  * 단순성 : 얼마나 단순한가
  * 최적성 : 더 이상 개선할 여지없이 최적화되었는가

#### 시간 복잡도 (Time Complexity)

* 실제 걸리는 시간 측정
* 실행되는 명령문 개수 계산
* 빅-오 표기법(Big-Oh Notation)
  * 시간 복잡도 함수 중 가장 큰 영향력을 주는 n에 대한 항만 표시
  * 계수(Coefficient)는 생략하여 표시



* 웬만하면 출력 함수 외에 내장함수 사용하지 말자(내장함수 사용금지 조건도 포함되기도 함)



### 배열

* 일정한 자료형의 변수들을 하나의 이름으로 열거하여 사용하는 자료구조
* 배열의 필요성

  * 프로그램 내에서 여러 개의 변수가 필요할 때, 일일이 다른 변수명을 이용하여 자료에 접근하는 것은 매우 비효율적일 수 있다.

  * 배열 사용 시 하나의 선언을 통해서 둘 이상의 변수 선언 가능

  * 다수의 변수로는 하기 힘든 작업을 배열을 활용해 쉽게 가능




### 정렬(Sort)

* 2개 이상의 자료를 특정 기준에 의해 오름차순 또는 내림차순 등으로 재배열하는 것
* 키 : 자료를 정렬하는 기준이 되는 특정 값
* 대표적인 정렬방식 종류
  * 버블 정렬(Bubble Sort)
  * 카운팅 정렬(Counting Sort)
  * 선택 정렬(Selection Sort)
  * 퀵 정렬(Quick Sort)
  * 삽입 정렬(Insertion Sort)
  * 병합 정렬(Merge Sort)

#### 버블 정렬(Bubble Sort)

* 인접한 두 개의 원소를 비교하며 자리를 계속 교환하는 방식
* 정렬 과정
  * 첫번째 원소부터 인접한 원소끼리 계속 자리를 교환하면서 맨 마지막 자리까지 이동
  * 한 단계가 끝나면 가장 큰 원소가 마지막 자리로 정렬
  * 교환하며 자리를 이동하는 모습이 물 위에 올라오는 거품 모양과 같다고 하여 버블 정렬이라고 함
* 시간 복잡도 : O(n^2)

```python
# 오름차순
N = int(input())				   # 입력 : 5
a = list(map(int,input().split())) # 	   55 7 78 12 42

for i in range(N-1, 0, -1):  # 각 구간의 끝
    for j in range(0, i):	 # 비교할 왼쪽 원소
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]  # 큰 원소를 오른쪽으로 이동
            
print(a) # [7, 12, 42, 55, 78]
```

````python
# 테스트 케이스가 여러 개라면? (가장 값이 큰 원소 호출)
```
3
5
55 7 78 12 42
6
55 7 78 12 42 90
7
55 7 78 12 42 90 100
```

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    a = list(map(int,input().split()))
    maxV = a[0]
    for i in range(1,N):
        if maxV < a[i]:
            maxV = a[i]
    print(f'#{tc} {maxV}')# #1 78
  							#2 90
  							#3 100
````
