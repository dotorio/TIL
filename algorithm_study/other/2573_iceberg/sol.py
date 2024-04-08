import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
ices = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def f(ices, time):
    next = []
    split = False
    visited = [[False]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if ices[i][j]:
                cnt = 0
                for k in range(4):
                    if 0<=i+dx[k]<N and 0<=j+dy[k]<M and not ices[i+dx[k]][j+dy[k]]:
                        cnt += 1
                next.append((i, j, cnt))
                if split and not visited[i][j]:
                    return time
                elif not split and not visited[i][j]:
                    split = True
                    stack = [(i, j)]
                    while stack:
                        now = stack.pop()
                        visited[now[0]][now[1]] = True
                        for k in range(4):
                            if 0<=now[0]+dx[k]<N and 0<=now[1]+dy[k]<M and ices[now[0]+dx[k]][now[1]+dy[k]] and not visited[now[0]+dx[k]][now[1]+dy[k]]:
                                stack.append((now[0]+dx[k], now[1]+dy[k]))
    for i in range(N):
        if True in visited[i]:
            break
        if i == N-1:
            return 0
    while next:
        i, j, cnt = next.pop()
        ices[i][j] = max(0, ices[i][j]-cnt)
    return f(ices, time+1)

print(f(ices, 0))