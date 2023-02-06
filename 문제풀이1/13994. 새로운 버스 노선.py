T = int(input())
 
for test_case in range(1, T+1):
    N = int(input())
    stop = [0] * 1001
    for i in range(N):
        num, a, b = map(int,input().split())
        stop[a] += 1
        stop[b] += 1
        for j in range(a+1, b):
            if num == 1:
                stop[j] += 1
 
            elif num == 2:
                if a % 2 == 0:
                    if j % 2 == 0:
                        stop[j] += 1
                else:
                    if j % 2 == 1:
                        stop[j] += 1
 
            elif num == 3:
                if a % 2 == 0:
                    if j % 4 == 0:
                        stop[j] += 1
                else:
                    if j % 3 == 0 and j % 10 != 0:
                        stop[j] += 1
 
    print(f'#{test_case} {max(stop)}')