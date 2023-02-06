T = int(input())
 
for test_case in range(1,T+1):
    N = int(input())
    num = list(map(int,input().split()))
    max_cnt = cnt = 1
    for i in range(N-1):
        if num[i] > num[i+1]:
            cnt = 1
        else:
            cnt += 1
            if cnt > max_cnt:
                max_cnt = cnt
 
    print(f'#{test_case} {max_cnt}')