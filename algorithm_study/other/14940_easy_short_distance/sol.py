import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(N)]
visited = [[-1]*M for _ in range(N)]
for i in range(N):
    if 2 in map[i]:
        start_x, start_y = i, map[i].index(2)
for i in range(N):
    for j in range(M):
        if map[i][j] == 0:
            visited[i][j] = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ctn = True
stack = [[[start_x, start_y]]]
cnt = 0
visited[start_x][start_y] = 0
while stack:
    next_cnt = stack.pop()
    cnt += 1
    linked = []
    while next_cnt:
        now = next_cnt.pop()
        for i in range(4):
            next_x, next_y = now[0] + dx[i], now[1] + dy[i]
            if 0 <= next_x < N and 0 <= next_y < M:
                if map[next_x][next_y] == 1 and visited[next_x][next_y] == -1:
                    visited[next_x][next_y] = cnt
                    linked.append([next_x, next_y])
    if linked != []:
        stack.append(linked)
for i in visited:
    print(*i)