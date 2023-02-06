for i in range(10):
    N = int(input())
    floor = list(map(int,input().split()))
    count = 0
    for j in range(2,N-2):
        a = floor[j] - floor[j-2]
        b = floor[j] - floor[j-1]
        c = floor[j] - floor[j+1]
        d = floor[j] - floor[j+2]
        if a > 0 and b > 0 and c > 0 and d > 0:
            count += min(a, b, c, d)
    print(f'#{i+1} {count}')