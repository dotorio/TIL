import sys
sys.stdin = open('input.txt')

dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, 1, -1]

for tc in range(int(input())):
    N, M = map(int, input().split())
    space = [list(map(int, input().split())) for _ in range(N)]
    stf = 0
    for i in range(N):
        for j in range(M):
            cnt = 0
            for k in range(8):
                if 0 <= i+dx[k] < N and 0 <= j+dy[k] < M and space[i][j] > space[i+dx[k]][j+dy[k]]:
                    cnt += 1
            if cnt >= 4:
                stf += 1
    print(f'#{tc+1} {stf}')