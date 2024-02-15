import sys
sys.stdin = open('input.txt')

board = [list(map(int, input().split())) for _ in range(5)]
game = [list(map(int, input().split())) for _ in range(5)]
result = False
cnt = 0
bingo = 0
jwapyo = {}
for i in range(5):
    for j in range(5):
        jwapyo[board[i][j]] = [i,j]
for i in range(5):
    for j in range(5):
        num_idx = jwapyo[game[i][j]]
        board[num_idx[0]][num_idx[1]] = 0
        cnt += 1
        if cnt >= 5:
            if sum(board[num_idx[0]]) == 0:
                bingo += 1
            if sum(board[k][num_idx[1]] for k in range(5)) == 0:
                bingo += 1
            if num_idx[0] == num_idx[1]:
                if sum(board[k][k] for k in range(5)) == 0:
                    bingo += 1
            if num_idx[0] == 4-num_idx[1]:
                if sum(board[k][4-k] for k in range(5)) == 0:
                    bingo += 1
            if bingo >= 3:
                result = True
                break
    if result == True:
        break
print(cnt)
