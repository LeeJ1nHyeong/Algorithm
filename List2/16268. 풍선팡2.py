T = int(input())
 
for test_case in range(1, T+1):
    N, M = map(int,input().split())
    balloon_list = [list(map(int,input().split())) for _ in range(N)]
    max_pang = 0
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    for i in range(N):
        for j in range(M):
            pang = 0
            pang += balloon_list[i][j]
            for k in range(4):
                ni, nj = i + di[k], j + dj[k]
                if 0 <= ni < N and 0 <= nj < M:
                    pang += balloon_list[ni][nj]
            if pang > max_pang:
                max_pang = pang
 
    print(f'#{test_case} {max_pang}')