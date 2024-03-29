N = int(input())
arr = list(map(int, input().split()))
arr2 = [0]*N
for i in range(N):
    min_num = 1000
    for j in range(i):
        if arr[i] > arr[j]:
            min_num = min(min_num, arr[j])
            

