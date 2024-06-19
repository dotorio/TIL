import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
red, blue = [], []
for i in range(1, N-1):
    for j in range(1, M-1):
        if board[i][j] == 'R':
            red.append((i, j))
        elif board[i][j] == 'B':
            blue.append((i, j))
        elif board[i][j] == 'O':
            hole = (i, j)

past, now, next = [], [(red[0], blue[0])], []
out = False

def f(fir, sec, dir):
    global out
    if out:
        return
    red_esc, blue_esc = False, False
    if dir == 1:
        for j in range(fir[1], 0, -1):
            if (fir[0], j) == hole:
                if fir == r:
                    red_esc = True
                else:
                    blue_esc = True
                new_fir = (-1, -1)
                break
            if board[fir[0]][j-1] == '#':
                new_fir = (fir[0], j)
                break
        else:
            new_fir = fir
        for j in range(sec[1], 0, -1):
            if (sec[0], j) == hole:
                if sec == r:
                    red_esc = True
                else:
                    blue_esc = True
                new_sec = (-1, -1)
                break
            if board[sec[0]][j-1] == '#' or (sec[0], j-1) == new_fir:
                new_sec = (sec[0], j)
                break
        else:
            new_sec = sec
    elif dir == 2:
        for j in range(fir[1], M-1):
            if (fir[0], j) == hole:
                if fir == r:
                    red_esc = True
                else:
                    blue_esc = True
                new_fir = (-1, -1)
                break
            if board[fir[0]][j+1] == '#':
                new_fir = (fir[0], j)
                break
        else:
            new_fir = fir
        for j in range(sec[1], M-1):
            if (sec[0], j) == hole:
                if sec == r:
                    red_esc = True
                else:
                    blue_esc = True
                new_sec = (-1, -1)
                break
            if board[sec[0]][j+1] == '#' or (sec[0], j+1) == new_fir:
                new_sec = (sec[0], j)
                break
        else:
            new_sec = sec
    elif dir == 3:
        for i in range(fir[0], 0, -1):
            if (i, fir[1]) == hole:
                if fir == r:
                    red_esc = True
                else:
                    blue_esc = True
                new_fir = (-1, -1)
                break
            if board[i-1][fir[1]] == '#':
                new_fir = (i, fir[1])
                break
        else:
            new_fir = fir
        for i in range(sec[0], 0, -1):
            if (i, sec[1]) == hole:
                if sec == r:
                    red_esc = True
                else:
                    blue_esc = True
                new_sec = (-1, -1)
                break
            if board[i-1][sec[1]] == '#' or (i-1, sec[1]) == new_fir:
                new_sec = (i, sec[1])
                break
        else:
            new_sec = sec
    else:
        for i in range(fir[0], N-1):
            if (i, fir[1]) == hole:
                if fir == r:
                    red_esc = True
                else:
                    blue_esc = True
                new_fir = (-1, -1)
                break
            if board[i+1][fir[1]] == '#':
                new_fir = (i, fir[1])
                break
        else:
            new_fir = fir
        for i in range(sec[0], N-1):
            if (i, sec[1]) == hole:
                if sec == r:
                    red_esc = True
                else:
                    blue_esc = True
                new_sec = (-1, -1)
                break
            if board[i+1][sec[1]] == '#' or (i+1, sec[1]) == new_fir:
                new_sec = (i, sec[1])
                break
        else:
            new_sec = sec
    if red_esc and not blue_esc:
        out = True
    elif not red_esc and not blue_esc:
        if fir == r:
            new = (new_fir, new_sec)
        else:
            new = (new_sec, new_fir)
        if new in past or new in now:
            return
        next.append(new)
    return

for time in range(1, 11):
    for loc in now:
        r, b = loc[0], loc[1]
        red_esc, blue_esc = False, False 
        # 만약 빨간 구슬, 파란 구슬이 같은 행에 있다면
        if r[0] == b[0]:
            if r[1] < b[1]:
                f(r, b, 1)
                f(b, r, 2)
            else:
                f(b, r, 1)
                f(r, b, 2)
        # 만약 빨간 구슬, 파란 구슬이 다른 행에 있다면
        else:
            f(r, b, 1)
            f(b, r, 2)
        # 만약 빨간 구슬, 파란 구슬이 같은 열에 있다면
        if r[1] == b[1]:
            if r[0] < b[0]:
                f(r, b, 3)
                f(b, r, 4)
            else:
                f(b, r, 3)
                f(r, b, 4)
        # 만약 빨간 구슬, 파란 구슬이 다른 열에 있다면
        else:
            f(r, b, 3)
            f(b, r, 4)
        if out:
            break
    past.extend(now)
    now = next
    next = []
    if out:
        print(time)
        break
    if not now:
        break
if not out:
    print(-1)