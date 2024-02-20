import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    ans = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] != 0:
                if i == 0 and j == 0:
                    pass
                elif i == 0:
                    if arr[i][j-1] != 0:
                        continue
                elif j == 0:
                    if arr[i-1][j] != 0:
                        continue
                else:
                    if arr[i][j-1] != 0 or arr[i-1][j] != 0:
                        continue
                col, row, x, y = 1, 1, i+1, j+1
                while x < n and arr[x][y-1] != 0:
                    col += 1
                    x += 1
                while y < n and arr[x-1][y] != 0:
                    row += 1
                    y += 1
                ans.append([col * row, col, row])
    ans.sort()
    print(f'#{tc} {len(ans)}', end = ' ')
    for i in ans:
        print(i[1], i[2], end = ' ')
    print()