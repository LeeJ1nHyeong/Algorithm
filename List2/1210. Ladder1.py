for _ in range(1,11):
    test_case = int(input())
    ladder = [list(map(int,input().split())) for _ in range(100)]
    idx = ladder[99].index(2)
    x = 99
    while x > 0:
        ladder[x][idx] = 0
        if idx == 0:
            if ladder[x][idx + 1] == 0:
                x -= 1
            elif ladder[x][idx + 1] == 1:
                idx += 1
 
        elif idx == 99:
            if ladder[x][idx - 1] == 0:
                x -= 1
            elif ladder[x][idx - 1] == 1:
                idx -= 1
 
        else:
            if ladder[x][idx - 1] == 0 and ladder[x][idx + 1] == 0:
                x -= 1
            elif ladder[x][idx - 1] == 1:
                idx -= 1
            elif ladder[x][idx + 1] == 1:
                idx += 1
 
    print(f'#{test_case} {idx}')