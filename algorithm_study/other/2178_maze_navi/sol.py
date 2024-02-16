import sys
sys.stdin = open('input.txt')
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
queue = deque([[[0,0]]])
visited[0][0] = 1
cnt = 1
result = False
while queue:
    next = queue.pop()
    cnt += 1
    linked = []
    while next:
        now = next.pop()
        for i in range(4):
            next_x = now[0] + dx[i]
            next_y = now[1] + dy[i]
            if 0 <= next_x < N and 0 <= next_y < M:
                if next_x == N-1 and next_y == M-1:
                    result = True
                    print(cnt)
                    break
                elif maze[next_x][next_y] == 1 and visited[next_x][next_y] == 0:
                    visited[next_x][next_y] = 1
                    linked.append([next_x, next_y])
        if result == True:
            break
    if result == True:
        break
    if linked != []:
        queue.append(linked)
    