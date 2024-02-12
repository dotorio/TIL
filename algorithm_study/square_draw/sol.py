import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    field = [list(map(int, input().split())) for _ in range(N)]
    area = []
    for i1 in range(N-1):
        for j1 in range(N-1):
            for i2 in range(i1+1, N):
                for j2 in range(j1+1, N):
                    if field[i1][j1] == field[i2][j2]:
                        area.append((i2-i1)*(j2-j1))
    if area == []:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} {area.count(max(area))}')