import sys
sys.stdin = open('input.txt')

dx = [-1, 1, 1, -1]
dy = [1, 1, -1, -1]

def f(i, j, ds, dir, num):
    global max_ds
    if dir[0] and dir[0] == dir[2] and dir[1] == dir[3]:
        max_ds = max(max_ds, len(ds))
        return
    if loc[i][j] in ds:
        return
    dir[num] += 1
    ds.append(loc[i][j])
    if num == 3 and loc[i+dy[3]][j+dx[3]] not in ds:
        f(i+dy[3], j+dx[3], ds, dir, 3)
        ds.pop()
        dir[3] -= 1
    elif num == 2:
        if dir[0]==dir[2] and loc[i+dy[3]][j+dx[3]] not in ds:
            f(i+dy[3], j+dx[3], ds, dir, 3)
            ds.pop()
            dir[3] -= 1
        elif j+dx[2]<N and loc[i+dy[2]][j+dx[2]] not in ds:
            f(i+dy[2], j+dx[2], ds, dir, 2)
            ds.pop()
            dir[2] -= 1
        else:
            return
    elif num == 1:
        if i+dy[1]<N and j+dx[1]<N and loc[i+dy[1]][j+dx[1]] not in ds:
            f(i+dy[1], j+dx[1], ds, dir, 1)
            ds.pop()
            dir[1] -= 1
        if j+dx[2]<N and loc[i+dy[2]][j+dx[2]] not in ds:
            f(i+dy[2], j+dx[2], ds, dir, 2)
            ds.pop()
            dir[2] -= 1
        else:
            return
    else:
        if i+dy[0]<N and 0<=j+dx[0] and loc[i+dy[0]][j+dx[0]] not in ds:
            f(i+dy[0], j+dx[0], ds, dir, 0)
            ds.pop()
            dir[0] -= 1
        if i+dy[1]<N and loc[i+dy[1]][j+dx[1]] not in ds:
            f(i+dy[1], j+dx[1], ds, dir, 1)
            ds.pop()
            dir[1] -= 1
        else:
            return

for tc in range(1, int(input())+1):
    N = int(input())
    loc = [list(map(int, input().split())) for _ in range(N)]
    max_ds = 0
    find_max = False
    for i in range(N-2):
        for j in range(1, N-1):
            ds = {loc[i][j]}
            dir = [0, 0, 0, 0]
            f(i, j, ds, dir, 0)
            if max_ds == 2*(N-1):
                find_max = True
                break
        if find_max:
            break
    if not max_ds:
        print(f'#{tc} -1')
    else:
        print(f'#{tc} {max_ds}')