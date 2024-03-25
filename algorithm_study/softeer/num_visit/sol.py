import sys
sys.stdin = open('input.txt')

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def f(x, y, v, c):
    global cnt
    v[x][y] = True
    for i in range(m):
        if not c[i]:
            if [x+1, y+1] == go_to[i]:
                c[i] = True
                if i == m-1:
                    cnt += 1
                    return
            break
    for i in range(4):
        if 0<=x+dx[i]<n and 0<=y+dy[i]<n:
            if not v[x+dx[i]][y+dy[i]] and not arr[x+dx[i]][y+dy[i]]:
                f(x+dx[i], y+dy[i], v, c)
                v[x+dx[i]][y+dy[i]] = False
                for k in range(m-1, -1, -1):
                    if c[k]:
                        if [x+dx[i]+1, y+dy[i]+1] == go_to[k]:
                            c[k] = False
                        break

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
go_to = [list(map(int, input().split())) for _ in range(m)]
go_check = [False]*m
visit = [[False]*n for _ in range(n)]
cnt = 0
start_x, start_y = go_to[0]
f(start_x-1, start_y-1, visit, go_check)
print(cnt)