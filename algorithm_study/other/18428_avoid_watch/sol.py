import sys
sys.stdin = open('input.txt')

from itertools import combinations

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def f():
    if len(avoid) < 3:
        return 'YES'
    for sets in list(combinations(avoid, 3)):
        status = True
        for x, y in sets:
            cor[x][y] = 'O'
        for i, j in teacher:
            for k in range(4):
                go = 1
                while True:
                    if 0<=i+dx[k]*go<N and 0<=j+dy[k]*go<N:
                        x, y = i+dx[k]*go, j+dy[k]*go
                        if cor[x][y] == 'S':
                            status = False
                            break
                        elif cor[x][y] in ['O', 'T']:
                            break
                        else:
                            go += 1
                            continue
                    else:
                        break
                if not status:
                    break
            if not status:
                break
        if status:
            return 'YES'
        for x, y in sets:
            cor[x][y] = 'X'
    return 'NO'


N = int(input())
cor = [list(input().split()) for _ in range(N)]
avoid, teacher = [], []
visited = [[False]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if cor[i][j] == 'T':
            teacher.append((i, j))
        elif cor[i][j] == 'X':
            avoid.append((i, j))
print(f())