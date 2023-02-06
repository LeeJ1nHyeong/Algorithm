T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    a = list(str(input()))
    num_count = [0] * 10
    for num in a:
        num_count[int(num)] += 1
 
    if num_count.count(max(num_count)) >= 2:
        max_list = []
        for i in range(9):
            if num_count[i] == max(num_count):
                max_list.append(i)
        print(f'#{test_case} {max(max_list)} {max(num_count)}')
    else:
        print(f'#{test_case} {num_count.index(max(num_count))} {max(num_count)}')