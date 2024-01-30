import sys
sys.stdin = open('input1.txt')

T = int(input())
for i in range(T):
    N, M = map(int, input().split())
    arr = [[0 for j in range(M)] for i in range(N)]
    for i2 in range(N):
        arr[i2] = list(map(int, input().split()))
    sum_list = []
    for y in range(N):
        for x in range(M):
            sum_flower = 0
            sum_flower += arr[y][x]
            if 0 <= x-1 < M:
                sum_flower += arr[y][x-1]
            if 0 <= x+1 < M:
                sum_flower += arr[y][x+1]
            if 0 <= y-1 < N:
                sum_flower += arr[y-1][x]
            if 0 <= y+1 < N:
                sum_flower += arr[y+1][x]
            sum_list.append(sum_flower)
    print(f'#{i+1} {max(sum_list)}')
