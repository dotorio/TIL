import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    for j in range(N):
        i = 0
        magnet = False
        while i < N:
            if table[i][j] == 1:
                magnet = True
            elif table[i][j] == 2 and magnet == True:
                cnt += 1
                magnet = False
            i += 1
    print(f'#{tc} {cnt}')