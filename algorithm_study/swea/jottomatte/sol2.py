import sys
sys.stdin = open('input.txt')
from queue import Queue

dy = [0, -1, 1, 0, 0]
dx = [0, 0, 0, -1, 1]

pipe = {1 : [1, 2, 3, 4],
        2 : [1 ,2, 0, 0],
        3 : [0, 0, 3, 4],
        4 : [1, 0, 0, 4],
        5 : [0, 2, 0, 4],
        6 : [0, 2, 3, 0],
        7 : [1, 0, 3, 0]}

def run(N, M, R, C, L, tunnel):
    visit = [[0]*M for _ in range(N)]
    can = 0
    loc = Queue()
    loc.put([R, C, 1])
    while loc:
        y, x, num = loc.get()
        if not visit[y][x]:
            visit[y][x] = 1
            can += 1
        if num == L:
            continue
        for i in pipe[tunnel[y][x]]:
            if i:
                y2, x2 = y+dy[i], x+dx[i]
                if 0<=y2<N and 0<=x2<M and tunnel[y2][x2] and not visit[y2][x2]:
                    if i == 1 and 2 in pipe[tunnel[y2][x2]]:
                        loc.put([y2, x2, num+1])
                    elif i == 2 and 1 in pipe[tunnel[y2][x2]]:
                        loc.put([y2, x2, num+1])
                    elif i == 3 and 4 in pipe[tunnel[y2][x2]]:
                        loc.put([y2, x2, num+1])
                    elif i == 4 and 3 in pipe[tunnel[y2][x2]]:
                        loc.put([y2, x2, num+1])
    return can

for tc in range(1, int(input())+1):
    N, M, R, C, L = map(int, input().split())
    tunnel = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{tc} {run(N, M, R, C, L, tunnel)}')