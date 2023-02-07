T = int(input())
 
for test_case in range(1,T+1):
    N = int(input())
    snail = [[0 for _ in range(N)] for _ in range(N)]
    snail[0][0] = 1
    x, y = 0, 0
    a = 0
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
 
    for i in range(2, N*N + 1):
        nx, ny = x + dx[a], y + dy[a]
        if  nx < 0 or nx >= N or ny < 0 or ny >= N or snail[nx][ny] != 0:
            if a == 3:
                a = 0
            else:
                a += 1
            nx, ny = x + dx[a], y + dy[a]
        snail[nx][ny] = i
        x, y = nx, ny
 
    print(f'#{test_case}')
    for i in snail:
        for j in i:
            print(j, end=' ')
        print()