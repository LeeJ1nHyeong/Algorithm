for _ in range(1, 11):
    test_case = int(input())
    num_list = [list(map(int,input().split())) for _ in range(100)]
    sum_list = []
    for i in range(100):
        sum_list.append(sum(num_list[i]))
        n = 0
        a = 0
        while n < 100:
            a += num_list[n][i]
            n += 1
        sum_list.append(a)
 
    cross1 = cross2 = 0
    for i in range(100):
        cross1 += num_list[i][i]
        cross2 += num_list[i][99 - i]
 
    num_list.append(cross1)
    num_list.append(cross2)
 
    print(f'#{test_case} {max(sum_list)}')