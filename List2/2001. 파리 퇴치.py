T = int(input())
 
for test_case in range(1, T+1):
    N, M = map(int,input().split())
    num_list = [list(map(int,input().split())) for _ in range(N)]
    max_fly_cnt = 0
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            fly_cnt = 0
            for k in range(M):
                for l in range(M):
                    fly_cnt += num_list[i + k][j + l]
                    if fly_cnt > max_fly_cnt:
                        max_fly_cnt = fly_cnt
 
    print(f'#{test_case} {max_fly_cnt}')