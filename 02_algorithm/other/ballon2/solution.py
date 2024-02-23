import sys
sys.stdin = open('input1.txt')

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for tc in range(int(input())):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_sum = 0
    for i in range(N):
        for j in range(M):
            sum = arr[i][j]
            for k in range(4):
                if 0 <= i+dx[k] < N and 0 <= j+dy[k] < M:
                    sum += arr[i+dx[k]][j+dy[k]]
            max_sum = max(max_sum, sum)
    print(f'#{tc+1} {max_sum}')
