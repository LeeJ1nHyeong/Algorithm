for test_case in range(1, 11):
    N = int(input())
    array = [list(map(int,input().split())) for _ in range(N)]
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    sum_abs = 0
    for i in range(N):
        for j in range(N):
            for k in range(4):
                ni, nj = i + di[k], j + dj[k]
                if 0 <= ni < N and 0 <= nj < N:
                    sum_abs += abs(array[i][j] - array[ni][nj])
 
    print(f'#{test_case} {sum_abs}')