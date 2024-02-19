import sys
sys.stdin = open('input.txt')

N = int(input())
pic = [list(map(str, input())) for _ in range(N)]
pic_bli = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if pic[i][j] == 'G':
            pic_bli[i][j] = 'R'
        else:
            pic_bli[i][j] = pic[i][j]
vis = [[0]*N for _ in range(N)]
vis_bli = [[0]*N for _ in range(N)]

def f(A, B):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if B[i][j] != 1:
                B[i][j] = 1
                stack = [[[i,j]]]
                cnt += 1
                while stack:
                    next = stack.pop()
                    linked = []
                    while next:
                        now = next.pop()
                        for k in range(4):
                            next_x = now[0] + dx[k]
                            next_y = now[1] + dy[k]
                            if 0 <= next_x < N and 0 <= next_y < N and B[next_x][next_y] != 1 and A[next_x][next_y] == A[i][j]:
                                B[next_x][next_y] = 1
                                linked.append([next_x,next_y])
                    if linked != []:
                        stack.append(linked)
    return cnt


com = f(pic, vis)
bli = f(pic_bli, vis_bli)
print(com, bli)
