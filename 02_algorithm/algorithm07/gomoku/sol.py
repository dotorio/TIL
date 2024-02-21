import sys
sys.stdin = open('input.txt')

def gomoku(board):
    for i in range(N-4):
        for j in range(N):
            x = i
            y = j
            if board[x][y] == 'o':
                cnt = 1
                x += 1
                while board[x][y] == 'o':
                    cnt += 1
                    if cnt == 5:
                        return 'YES'
                    x += 1
    for i in range(N):
        for j in range(N-4):
            x = i
            y = j
            if board[x][y] == 'o':
                cnt = 1
                y += 1
                while board[x][y] == 'o':
                    cnt += 1
                    if cnt == 5:
                        return 'YES'
                    y += 1   
    for i in range(N-4):
        for j in range(N-4):
            x = i
            y = j
            if board[x][y] == 'o':
                cnt = 1
                x += 1
                y += 1
                while board[x][y] == 'o':
                    cnt += 1
                    if cnt == 5:
                        return 'YES'
                    x += 1
                    y += 1    
    for i in range(N-1, 3, -1):
        for j in range(N-4):
            x = i
            y = j
            if board[x][y] == 'o':
                cnt = 1
                x -= 1
                y += 1
                while board[x][y] == 'o':
                    cnt += 1
                    if cnt == 5:
                        return 'YES'
                    x -= 1
                    y += 1   
    return 'NO'            

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    board = [list(input()) for _ in range(N)]
    print(f'#{tc} {gomoku(board)}')