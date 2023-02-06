T = int(input())
 
for test_case in range(1,T+1):
    N = int(input())
    temp = N
    a = b = c = d = e = 0
 
    while temp%2 == 0:
        temp /= 2
        a += 1
 
    while temp%3 == 0:
        temp /= 3
        b += 1
 
    while temp%5 == 0:
        temp /= 5
        c += 1
 
    while temp%7 == 0:
        temp /= 7
        d += 1
 
    while temp%11 == 0:
        temp /= 11
        e += 1
 
    print(f'#{test_case} {a} {b} {c} {d} {e}')