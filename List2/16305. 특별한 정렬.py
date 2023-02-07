T = int(input())
 
for test_case in range(1, T+1):
    N = int(input())
    num_list = list(map(int,input().split()))
    special = [0 for _ in range(N)]
    for i in range(N-1):
        idx = i
        for j in range(i+1, N):
            if num_list[idx] > num_list[j]:
                idx = j
        num_list[i], num_list[idx] = num_list[idx], num_list[i]
 
    if N%2 == 0:
        for i in range(int(N/2)):
            special[2*i] = num_list[N - i -1]
            special[2*i+1] = num_list[i]
 
    else:
        special[N - 1] = num_list[int(N/2)]
        for i in range(int(N/2)):
            special[2 * i] = num_list[N - i - 1]
            special[2 * i + 1] = num_list[i]
 
    print(f'#{test_case}', end = ' ')
    for i in range(10):
        print(special[i], end=' ')
    print()