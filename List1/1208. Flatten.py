for test_case in range(10):
    dump = int(input())
    height = list(map(int,input().split()))
    dump_trial = 0
 
    for i in range(dump):
        max_h = max(height)
        min_h = min(height)
 
        max_index = height.index(max_h)
        min_index = height.index(min_h)
 
        height[max_index] -= 1
        height[min_index] += 1
 
    print(f'#{test_case+1} {max(height) - min(height)}')