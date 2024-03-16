import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input())+1):
    N, X = map(int, input().split())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    con = 0
    for i in range(N):
        can = True
        base = MAP[i][0]
        j, equal = 1, 0
        while j != N:
            if base != MAP[i][j]:
                if abs(base-MAP[i][j]) != 1:
                    can = False
                    break
                elif base-MAP[i][j] == 1:
                    for k in range(1, X):
                        if j+k >= N or (j+k < N and MAP[i][j] != MAP[i][j+k]):
                            can = False
                            break
                    if not can:
                        break
                    j = min(N, j+X)
                else:
                    if equal < X-1:
                        can = False
                        break
                    j += 1
                if j < N:
                    base, equal = MAP[i][j-1], 0
            else:
                j += 1
                equal += 1        
        if can:
            con += 1
    for j in range(N):
        can = True
        base = MAP[0][j]
        i, equal = 1, 0
        while i != N:
            if base != MAP[i][j]:
                if abs(base-MAP[i][j]) != 1:
                    can = False
                    break
                elif base-MAP[i][j] == 1:
                    for k in range(1, X):
                        if i+k >= N or (i+k < N and MAP[i][j] != MAP[i+k][j]):
                            can = False
                            break
                    if not can:
                        break
                    i = min(N, i+X)
                else:
                    if equal < X-1:
                        can = False
                        break
                    i += 1
                if i < N:
                    base, equal = MAP[i][j], 0
            else:
                i += 1 
                equal += 1       
        if can:
            con += 1    
    print(f'#{tc} {con}')