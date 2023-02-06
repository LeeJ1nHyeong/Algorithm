T = int(input())
 
for test_case in range(1,T+1):
    N = int(input())
    num = list(map(int,input()))
    max_cnt = 0
    cnt = 0
    for i in range(N):
        if num[i] == 0:
            cnt = 0
        else:
            cnt += 1
            if cnt > max_cnt:
                max_cnt = cnt
 
    print(f'#{test_case} {max_cnt}')