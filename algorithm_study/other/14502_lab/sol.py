import sys
sys.stdin = open('input.txt')

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def g(arr):
    global max_safe
    visited = [[False]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 2 and not visited[i][j]:
                stack = [(i, j)]
                while stack:
                    now = stack.pop()
                    visited[now[0]][now[1]] = True
                    for k in range(4):
                        if 0 <= now[0] + dx[k] < N and 0 <= now[1] + dy[k] < M and not visited[now[0] + dx[k]][now[1] + dy[k]]:
                            if arr[now[0] + dx[k]][now[1] + dy[k]] != 1:
                                stack.append((now[0] + dx[k], now[1] + dy[k]))

            elif arr[i][j] == 1:
                visited[i][j] = True
    cnt = 0
    for i in visited:
        cnt += i.count(False)
    max_safe = max(max_safe, cnt)

def f(i, j, arr, wall):
    if wall == 3:
        return g(arr)
    elif arr[i][j] == 0:
        arr[i][j] = 1
        if (i, j) == (N-1, M-1):
            if wall+1 != 3:
                arr[i][j] = 0
                return
            else:
                g(arr)
                arr[i][j] = 0
                return
        elif j == M-1:
            new_i, new_j = i+1, 0
        else:
            new_i, new_j = i, j+1
        f(new_i, new_j, arr, wall+1)
        arr[i][j] = 0
        return f(new_i, new_j, arr, wall)
    else:
        if (i, j) == (N-1, M-1):
            return
        elif j == M-1:
            i, j = i+1, 0
        else:
            j += 1
        return f(i, j, arr, wall)
    

N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
max_safe = 0
f(0, 0, arr, 0)
print(max_safe)