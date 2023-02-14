# 2/7(화)

## 검색

* 저장되어 있는 자료 중에서 원하는 항목을 찾는 작업
* 목적하는 탐색 키를 가진 항목을 찾는 것
  * 탐색 키(Search Key) : 자료를 구별하여 인식할 수 있는 키
* 검색의 종류
  * 순차 검색(Sequential Search)
  * 이진 검색(Binary Search)
  * 해쉬(Hash)



### 순차 검색(Sequential Search)

* 일렬로 되어 있는 자료를 순서대로 검색하는 방법

  * 가장 간단하고 직관적인 검색 방법

  * 배열이나 연결 리스트 등 순차구조로 구현된 자료구조에서 원하는 항목을 찾을 때 유용함

  * 단순한 알고리즘 → 구현이 쉬움

    but 검색 대상 수가 많은 경우 수행시간 급격히 증가

* 정렬되어 있지 않은 경우

  * 첫 번째 원소부터 순서대로 검색 대상과 키 값이 같은 원소가 있는지 비교하며 찾는다.
  * 키 값이 동일한 원소를 찾으면 그 원소의 인덱스 반환
  * 자료구조의 마지막에 이를 때까지 검색 대상을 찾지 못하면 검색 실패
  * 찾고자 하는 원소 순서에 따라 비교회수 결정
  * 시간 복잡도 : O(n)

  ```python
  def sequentialSearch(a, n, key):  # 정렬 X인 경우
      i = 0
      while i < n and a[i] != key:  # 순서 주의
          i += 1
      if i < n :
          return i
      else:
          return -1
  ```

* 정렬되어 있는 경우(오름차순 가정)

  * 자료를 순차적으로 검색하면서 키 값 비교

    → 원소 키 값이 검색 대상 키 값보다 크면 찾는 원소가 없다는 뜻

    → 더 이상 검색 진행 않고 종료

  * 찾고자 하는 원소 순서에 따라 비교회수 결정

  * 시간 복잡도 : O(n)

  ```python
  def sequentialSearch2(a, n, key):  # 정렬 O인 경우
      i = 0
      while i < n and a[i] < key:
          i += 1
      if i < n and a[i] == key:
          return i
      else:
          return -1
  ```



### 이진 검색(Binary Search)

* 자료의 가운데에 있는 항목의 키 값과 비교하여 다음 검색의 위치를 결정하고 검색을 계속 진행하는 방법

  * 목적 키를 찾을 때까지 이진 검색을 순환적으로 반복 수행함으로써 검색 범위를 반으로 줄여가면서 보다 빠르게 검색을 수행함

* 자료가 정렬된 상태여야 한다.

* 검색 과정

  * 자료의 중앙에 있는 원소를 고른다.
  * 중앙 원소 값과 찾고자 하는 목표 값을 비교한다.
  * 목표 값이 중앙 원소 값보다 작으면 자료의 왼쪽 반에 대해 새로 검색을 수행하고, 크다면 자료의 오른쪽 반에 대해서 새로 검색을 수행한다.
  * 원하는 값을 찾을 때까지 위 과정을 반복한다.

* 구현

  * 검색 범위 시작점과 종료점을 이용하여 검색 반복 수행
  * 자료에 삽입이나 삭제가 발생했을 때 배열 상태를 항상 정렬상태로 유지하는 추가 작업 필요

  ```python
  def binarySearch(a, N, key):  # 이진 검색 알고리즘
      start = 0
      end = N - 1
      while start <= end:
          middle = (start + end) // 2
          if a[middle] == key :  # 검색 성공 시
              return True
          elif a[middle] > key:
              end = middle - 1
          else:
              start = middle + 1
      return false  # 검색 실패 시
  ```

  

### 인덱스(Index)

* Database에서 유래했으며, 테이블에 대한 동작 속도를 높여주는 자료구조를 일컫는 말

* 배열을 사용한 인데긋

  * 대량의 데이터를 매번 정렬 시, 프로그램 반응은 느려짐

    → 대량의 데이터 성능 저하문제 해결을 위해 배열 인덱스 사용



### 선택 정렬(Selection Sort)

* 주어진 자료들 중 가장 작은 값의 원소부터 차례대로 선택하여 위치를 교환하는 방식

* 정렬 과정

  * 주어진 리스트 중 최소값을 찾는다.
  * 그 값을 리스트의 맨 앞에 위치한 값과 교환한다.
  * 맨 처음 위치를 제외한 나머지 리스트를 대상으로 위 과정 반복

* 시간 복잡도 : O(n2)

  ```python
  def selectionSort(a, N):
      for i in range(N-1):
          minIdx = i
          for j in range(i+1, N):
              if a[minIdx] > a[j]:
                  minIdx = j
          a[i], a[minIdx] = a[minIdx], a[i]
  ```

  

### 셀렉션 알고리즘(Selection Algorithm)

* 저장되어 있는 자료로부터 k번째로 큰 혹은 작은 원소를 찾는 방법

  * 최소값, 최대값 혹은 중간값을 찾는 알고리즘

* 선택 과정

  * 정렬 알고리즘을 이용하여 자료 정렬
  * 원하는 순서에 있는 원소 가져오기

* k번째로 작은 원소를 찾는 알고리즘

  ```python
  def select(arr, k):
      for i in ragne(0, k):
          minIndex = i
          for j in range(i+1, len(arr)):
              if arr[minIndex] > arr[j]:
                  minIndex = j
          arr[i], arr[minIndex] = arr[minIndex], arr[i]
      return arr[k-1]
  ```

```python
'''
7
7 2 5 3 4 6 4
'''

N = int(input())
arr = list(map(int,input().split()))

for i in range(N-1):  # 작업 구간 시작 인덱스
    minIdx = i        # 맨 앞이 최소값이라고 가정
    for j in range(i+1, N):
        if arr[minIdx] > arr[j]:
            minIdx = j
    arr[minIdx], arr[i] = arr[i], arr[minIdx]

print(arr)  # [2, 3, 4, 4, 5, 6, 7]
```

