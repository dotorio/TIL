import sys
sys.stdin = open('input1.txt')

T = int(input())
for i in range(T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for i in range(N)]
    sum_list = []
    
    for y in range(N):
        for x in range(M):
            sum_flower = 0
            sum_flower += arr[y][x]
            for s in range(1, arr[y][x]+1):
                if 0 <= x-s < M:
                    sum_flower += arr[y][x-s]
                if 0 <= x+s < M:
                    sum_flower += arr[y][x+s]
                if 0 <= y-s < N:
                    sum_flower += arr[y-s][x]
                if 0 <= y+s < N:
                    sum_flower += arr[y+s][x]
            sum_list.append(sum_flower)
    print(f'#{i+1} {max(sum_list)}')