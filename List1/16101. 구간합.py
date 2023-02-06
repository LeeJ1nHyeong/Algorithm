T = int(input())
 
for i in range(1,T+1):
    N, M = map(int,input().split())
    num = list(map(int,input().split()))
    sum_list = []
    for j in range(N-M+1):
        a = 0
        for k in num[j:j+M]:
            a += k
        sum_list.append(a)
    min_sum = sum_list[0]
    max_sum = sum_list[0]
 
    for x in range(1,N-M+1):
        if sum_list[x] > max_sum:
            max_sum = sum_list[x]
        elif sum_list[x] < min_sum:
            min_sum = sum_list[x]
 
    print(f'#{i} {max_sum - min_sum}')