T = int(input())
  
for test_case in range(1,T+1):
    N = int(input())
    array = [list(map(int,input().split())) for _ in range(N)]
    a_90 = [[0 for _ in range(N)] for _ in range(N)]
    a_180 = [[0 for _ in range(N)] for _ in range(N)]
    a_270 = [[0 for _ in range(N)] for _ in range(N)]
  
    for i in range(N):
        for j in range(N):
            a_90[i][j] = array[N - j - 1][i]
            a_180[i][j] = array[N - i - 1][N - j - 1]
            a_270[i][j] = array[j][N - i - 1]
  
    print(f'#{test_case}')
    for i in range(N):
        for j in range(N):
            print(a_90[i][j], end='')
        print(end=' ')
        for j in range(N):
            print(a_180[i][j], end='')
        print(end=' ')
        for j in range(N):
            print(a_270[i][j], end='')
        print(end=' ')
        print()