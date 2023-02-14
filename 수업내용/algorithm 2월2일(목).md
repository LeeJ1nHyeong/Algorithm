# 2/2(목)

### 카운팅 정렬(Counting Sort)

* 항목들의 순서를 결정하기 위해 집합에 각 항목이 몇 개씩 있는지 세는 작업을 하여, 선형 시간에 정렬하는 효율적인 알고리즘
* 정수나 정수로 표현할 수 있는 자료에 대해서만 사용 가능

```python
data = [0, 4, 1, 3, 1, 2, 4, 1]
max = max(data)
count = [0] * (max + 1)
temp = [0] * len(data)

for i in range(len(data)):
    count[data[i]] += 1

print(count)  # [1, 3, 1, 1, 2]

for i in range(1,len(count)):
    count[i] += count[i-1]

print(count)  # [1, 4, 5, 6, 8]

for i in range(len(temp)-1, -1, -1):
    count[data[i]] -= 1
    temp[count[data[i]]] = data[i]

print(temp)  # [0, 1, 1, 1, 2, 3, 4, 4]
```



### Baby-gin Game

* 0 ~ 9 사이의 숫자 카드에서 임의의 카드 6장을 뽑았을 때, 3장의 카드가 연속적인 번호를 갖는 경우를 run, 3장의 카드가 동일한 번호를 갖는 경우 triplet이라고 한다.

* 6장의 카드가 run과 triplet로만 구성된 경우 baby-gin이라고 함

* 예시

  * 667767 → triplet 2개이므로 baby-gin (666, 777)

  * 054060 → run 1개 + triplet 1개이므로 baby-gin (456, 000)

  * 101123 → triplet 1개(111) but 023 암것도 아님 -> baby-gin X

     				 run 1개(123) but 011 암것도 아님 → baby-gin X

```python
c = [0] * 12 # 6자리 수로부터 각 자리 수를 추출하여 개수를 누적할 리스트

#print(num / 10)

for i in range(6) :
    #print(num % 10)  # 9
    c[num % 10] += 1 # c[9] += 1
    num //= 10
#   num = num / 10


print(c)

i = tri = run = 0
while i < 10 : #i = 0 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6 -> 7 -> 7 -> 8 -> 9 -> 10
    if c[i] >= 3 : # triplete 조사 후 데이터 삭제
        c[i] -= 3
        tri += 1
        continue;
    if c[i] >= 1 and c[i+1] >= 1 and c[i+2] >= 1 : # run 조사 후 데이터 삭제
        c[i] -= 1
        c[i+1] -= 1
        c[i+2] -= 1
        run += 1 # 1 2
        continue;
    i += 1

if run + tri == 2 : print("Baby Gin")
else : print("Lose")
```



