import sys
sys.stdin = open('input.txt')

dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    board = [[0]*N for _ in range(N)]
    board[N//2-1][N//2-1] = 2
    board[N//2-1][N//2] = 1
    board[N//2][N//2-1] = 1
    board[N//2][N//2] = 2
    for _ in range(M):
        x, y, c = map(int, input().split())
        board[y-1][x-1] = c
        if c == 1:
            new_c = 2
        else:
            new_c = 1
        for i in range(8):
            new_x, new_y = x+dx[i]-1, y+dy[i]-1
            if 0 <= new_x < N and 0 <= new_y < N:
                stack = []
                while board[new_y][new_x] == new_c:
                    stack.append([new_y, new_x])
                    new_x += dx[i]
                    new_y += dy[i]
                    if 0 <= new_x < N and 0 <= new_y < N:
                        pass
                    else:
                        break
                if 0 <= new_x < N and 0 <= new_y < N and board[new_y][new_x] == c:
                    while stack:
                        now = stack.pop()
                        board[now[0]][now[1]] = c
    sum_b = 0
    sum_w = 0
    for i in board:
        sum_b += i.count(1)
        sum_w += i.count(2)
    print(f'#{tc} {sum_b} {sum_w}')
