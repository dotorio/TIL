def f(i, j, board):
    global cnt
    for go in range(1, i+1):
        for k in range(3):
            if 0 <= j+dy[k]*go < N:
                if board[i+dx[k]*go][j+dy[k]*go]:
                    return
    if i == N-1:
        cnt += 1
        return
    for k in range(N):
        board[i+1][k] = True
        f(i+1, k, board)
        board[i+1][k] = False

N = int(input())
board = [[False]*N for _ in range(N)]
dx = [-1, -1, -1]
dy = [-1, 0, 1]
cnt = 0
for j in range(N):
    board[0][j] = True
    f(0, j, board)
    board[0][j] = False
print(cnt)
