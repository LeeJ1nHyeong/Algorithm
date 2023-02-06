T = int(input())
 
for i in range(1,T+1):
    N = int(input())
    a = list(map(int,input().split()))
    count_list = []
    max_count = 0
    for j in range(N-1):
        count = 0
        for k in range(j+1,N):
            if a[j] > a[k]:
                count += 1
        count_list.append(count)
 
    for count in count_list:
        if count > max_count:
            max_count = count
 
    print(f'#{i} {max_count}')