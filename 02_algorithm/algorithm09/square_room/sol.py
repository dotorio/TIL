import sys
sys.stdin = open('input.txt')

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for tc in range(1, int(input())+1):
    N = int(input())
    room = [list(map(int, input().split())) for _ in range(N)]
    move_cnt = [[0]*N for _ in range(N)]
    max_cnt = 0
    for i in range(N):
        for j in range(N):
            cnt = 1
            x, y = i, j
            the_num = room[i][j]
            result = True
            while result:
                result = False
                for k in range(4):
                    if 0 <= x+dx[k] < N and 0 <= y+dy[k] < N:
                        if room[x+dx[k]][y+dy[k]] == the_num + 1:
                            result = True
                            cnt += 1
                            the_num += 1
                            x, y = x+dx[k], y+dy[k]
                            break
                if not result:
                    move_cnt[i][j] = cnt
                    if max_cnt <= cnt:
                        max_cnt = max(cnt, max_cnt)
    min_room = 10000
    for i in range(N):
        for j in range(N):
            if move_cnt[i][j] == max_cnt:
                min_room = min(min_room, room[i][j])
    print(f'#{tc} {min_room} {max_cnt}')


