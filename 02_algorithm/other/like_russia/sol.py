import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    flag = [list(input()) for _ in range(N)]
    min_cnt = N*M
    for g1 in range(1, N-1):
        for g2 in range(g1+1, N):
            cnt = 0
            for c1 in range(g1):
                for j in range(M):
                    if flag[c1][j] != 'W':
                        cnt += 1
            for c2 in range(g1, g2):
                for j in range(M):
                    if flag[c2][j] != 'B':
                        cnt += 1
            for c3 in range(g2, N):
                for j in range(M):
                    if flag[c3][j] != 'R':
                        cnt += 1
            min_cnt = min(min_cnt, cnt)
    print(f'#{tc} {min_cnt}')
