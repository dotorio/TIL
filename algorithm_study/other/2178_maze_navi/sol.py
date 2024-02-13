import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
stack = [[0,0]]
visited[0][0] = 1
result = 0
cnt = 1
while stack:
    now = stack[-1]
    for i in range(4):
        next_x = now[0] + dx[i]
        next_y = now[1] + dy[i]
        if 0 <= next_x < N and 0 <= next_y < M:
            if next_x == N-1 and next_y == M-1:
                cnt += 1
                result = 1
                print(cnt)
                break
            elif maze[next_x][next_y] == 1 and visited[next_x][next_y] == 0:
                visited[next_x][next_y] = 1
                cnt += 1