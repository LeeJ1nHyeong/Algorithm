T = int(input())
 
for test_case in range(1, T+1):
    K, N, M = list(map(int, input().split()))
    charge_list = list(map(int, input().split()))
    count_stop = 0
    stop = 0
 
    while stop + K < N:
        for i in range(K, 0, -1):
            if (stop + i) in charge_list:
                stop += i
                count_stop += 1
                break
 
        else:
            count_stop = 0
            break
 
    print(f'#{test_case} {count_stop}')