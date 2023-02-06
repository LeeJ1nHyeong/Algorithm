T = int(input())
 
for i in range(1,T+1):
    N = int(input())
    max_num = 0
    min_num = 1000000
    num = list(map(int,input().split()))
    for j in num:
        if j > max_num:
            max_num = j
        elif j < min_num:
            min_num = j
 
    print(f'#{i} {max_num - min_num}')