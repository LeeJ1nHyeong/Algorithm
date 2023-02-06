T = int(input())
 
for test_case in range(1, T+1):
    N = int(input())
    num_list = list(map(int,input().split()))
    for i in range(N-1, 0 , -1):
        for j in range(0, i):
            if num_list[j] > num_list[j+1]:
                num_list[j], num_list[j+1] = num_list[j+1], num_list[j]
 
    print(f'#{test_case}', end=' ')
    for num in num_list:
        print(num,end=' ')
    print()