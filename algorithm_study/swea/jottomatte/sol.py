import sys
sys.stdin = open('input.txt')
from collections import deque

dy = [0, -1, 1, 0, 0]
dx = [0, 0, 0, -1, 1]

pipe = {1 : [[1, 2, 3, 4], [2, 1, 4, 3]],
        2 : [[1 ,2, 0, 0], [2, 1, 0, 0]],
        3 : [[0, 0, 3, 4], [0, 0, 4, 3]],
        4 : [[1, 0, 0, 4], [2, 0, 0, 3]],
        5 : [[0, 2, 0, 4], [0, 1, 0, 3]],
        6 : [[0, 2, 3, 0], [0, 1, 4, 0]],
        7 : [[1, 0, 3, 0], [2, 0, 4, 0]]}

def run(N, M, R, C, L, tunnel):
    visit = [[0]*M for _ in range(N)]
    can = 0
    loc = deque([[R, C, 1]])
    while loc:
        y, x, num = loc.popleft()
        visit[y][x] = 1
        can += 1
        if num == L:
            continue
        for i in pipe[tunnel[y][x]][0]:
            if i:
                y2, x2 = y+dy[i], x+dx[i]
                if 0<=y2<N and 0<=x2<M and tunnel[y2][x2] and not visit[y2][x2]:
                    if i == 1 and pipe[tunnel[y2][x2]][1][0] == 2:
                        loc.append([y2, x2, num+1])
                    elif i == 2 and pipe[tunnel[y2][x2]][1][1] == 1:
                        loc.append([y2, x2, num+1])
                    elif i == 3 and pipe[tunnel[y2][x2]][1][2] == 4:
                        loc.append([y2, x2, num+1])
                    elif i == 4 and pipe[tunnel[y2][x2]][1][3] == 3:
                        loc.append([y2, x2, num+1])
    return can

for tc in range(1, int(input())+1):
    N, M, R, C, L = map(int, input().split())
    tunnel = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{tc} {run(N, M, R, C, L, tunnel)}')