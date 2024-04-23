# def f(i, j, board):
#     global cnt
#     for go in range(1, i+1):
#         for k in range(3):
#             if 0 <= j+dy[k]*go < N:
#                 if board[i+dx[k]*go][j+dy[k]*go]:
#                     return
#     if i == N-1:
#         cnt += 1
#         return
#     for k in range(N):
#         board[i+1][k] = True
#         f(i+1, k, board)
#         board[i+1][k] = False

# N = int(input())
# board = [[False]*N for _ in range(N)]
# dx = [-1, -1, -1]
# dy = [-1, 0, 1]
# cnt = 0
# for j in range(N):
#     board[0][j] = True
#     f(0, j, board)
#     board[0][j] = False
# print(cnt)

N = int(input())
board = [-1]*N
if N%2:
    new_N = N//2+1
    button = True
else:
    new_N = N//2
    button = False
cnt = 0

def place(num):
    global cnt
    if num == N-1:
        if button and new_button:
            cnt += 1
        else:
            cnt += 2
        return
    else:
        for i in range(N):
            board[num+1] = i
            if check(num+1):
                place(num+1)

def check(num):
    for i in range(num):
        if board[i] == board[num] or abs(board[i] - board[num]) == abs(i - num):
            return False
    return True

for i in range(new_N):
    if button and i == new_N-1:
        new_button = True
    else:
        new_button = False
    board[0] = i
    place(0)

print(cnt)