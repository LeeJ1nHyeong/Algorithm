T = int(input())
 
for test_case in range(1, T+1):
    N = int(input())
    count = [0] * 5001
    for _ in range(N):
        A, B = map(int,input().split())
        for i in range(A, B+1):
            count[i] += 1
 
    P = int(input())
    alst = []
    for _ in range(P):
        C = int(input())
        alst.append(count[C])
 
    print(f'#{test_case}', *alst)