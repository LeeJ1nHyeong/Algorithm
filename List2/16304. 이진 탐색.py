T = int(input())
 
for test_case in range(1, T+1):
    P, Pa, Pb = map(int,input().split())
    l, r = 1, P
    cnt_a = cnt_b = 0
 
    while l <= r:  # A 이진 탐색
        cnt_a += 1
        c = int((l + r) / 2)
        if c == Pa:
            break
        elif c > Pa:
            r = c
        else:
            l = c
 
    l, r = 1, P
    while l <= r:  # B 이진 탐색
        cnt_b += 1
        c = int((l + r) / 2)
        if c == Pb:
            break
        elif c > Pb:
            r = c
        else:
            l = c
     
    # 승자 여부 판단
    if cnt_a < cnt_b:
        winner = 'A'
    elif cnt_a > cnt_b:
        winner = 'B'
    else:
        winner = 0
    print(f'#{test_case} {winner}')