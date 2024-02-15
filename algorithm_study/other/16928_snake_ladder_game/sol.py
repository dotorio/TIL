board = [0]*100
N, M = map(int, input().split())
for i in range(N):
    start, end = map(int, input().split())
    board[start-1] = 1000+i
    board[end-1] = 2000+i
for i in range(M):
    start, end = map(int, input().split())
    board[start-1] = 3000+i
    board[end-1] = 4000+i
