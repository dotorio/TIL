import sys
sys.stdin = open('input.txt')
from heapq import heappop, heappush

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for tc in range(1, int(input())+1):
    N = int(input())
    MAP = [list(map(int, input())) for _ in range(N)]
    visited = [[False]*N for _ in range(N)]
    pq = []
    heappush(pq, (0, 0, 0))
    while pq:
        time, i, j = heappop(pq)
        if (i, j) == (N-1, N-1):
            print(f'#{tc} {time}')
            break
        if visited[i][j]:
            continue
        visited[i][j] = True
        for k in range(4):
            if 0 <= i+dx[k] < N and 0 <= j+dy[k] < N:
                heappush(pq, (time + MAP[i+dx[k]][j+dy[k]], i+dx[k], j+dy[k]))