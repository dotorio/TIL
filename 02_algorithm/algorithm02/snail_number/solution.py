import sys
sys.stdin = open('input.txt')

T = int(input())

for case in range(1, T+1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    coo = [-1, 0]
    num = 1
    while N >= 1:
        for i in range(N):
            coo[0] += 1
            arr[coo[1]][coo[0]] = num
            num += 1
            
        for i in range(N-1):
            coo[1] += 1
            arr[coo[1]][coo[0]] = num
            num += 1
            
        for i in range(N-1):
            coo[0] -= 1
            arr[coo[1]][coo[0]] = num
            num += 1
            
        for i in range(N-2):
            coo[1] -= 1
            arr[coo[1]][coo[0]] = num
            num += 1
            
        N -= 2
    print(f'#{case}')
    for i in arr:

        print(" ".join(map(str, i)))