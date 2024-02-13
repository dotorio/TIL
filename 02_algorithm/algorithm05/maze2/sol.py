import sys
sys.stdin = open('input.txt')

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(10):
    tc = int(input())
    maze = [list(map(int, input())) for _ in range(100)]
    visited = [[0] * 100 for _ in range(100)]
    stack = []
    for x in range(100):
        if 2 in maze[x]:
            start_x = x
            start_y = maze[x].index(2)
            stack.append([start_x, start_y])
            break
    visited[start_x][start_y] = 1
    result = 0
    while stack:
        now = stack.pop()
        for i in range(4):
            if maze[now[0] + dx[i]][now[1] + dy[i]] == 0 and visited[now[0] + dx[i]][now[1] + dy[i]] == 0:
                visited[now[0] + dx[i]][now[1] + dy[i]] = 1
                stack.append([now[0] + dx[i], now[1] + dy[i]])
            elif maze[now[0] + dx[i]][now[1] + dy[i]] == 3:
                result = 1
                print(f'#{tc} {result}')
                break
        if result == 1:
            break
    if result == 0:
        print(f'#{tc} {result}')
    



    
    