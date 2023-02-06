T = int(input())
 
for test_case in range(1,T+1):
    array = [[0] * 10 for _ in range(10)]
    N = int(input())
    for _ in range(N):
        r1, c1, r2, c2, color = map(int,input().split())
        for i in range(r1,r2+1):
            for j in range(c1,c2+1):
                if color == 1:
                    if array[i][j] == 1:
                        continue
                    else:
                        array[i][j] += color
                elif color == 2:
                    if array[i][j] == 2:
                        continue
                    else:
                        array[i][j] += color
 
    purple = 0
    for i in range(10):
        for j in range(10):
            if array[i][j] == 3:
                purple += 1
 
    print(f'#{test_case} {purple}')