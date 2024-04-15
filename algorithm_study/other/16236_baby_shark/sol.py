import sys
sys.stdin = open('input.txt')

from collections import deque

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

N = int(input())
area = [list(map(int, input().split())) for _ in range(N)]
if_fish, time, baby_shark, cnt = False, 0, 2, 0
for i in range(N):
    for j in range(N):
        if area[i][j]:
            if area[i][j] == 9:
                baby_x, baby_y = i, j
                area[i][j] = 0
            else:
                if_fish = True
while if_fish:
    if_fish, fish_list = False, []
    visited = [[False]*N for _ in range(N)]
    min_dis = N**2
    find = deque()
    find.append((baby_x, baby_y, 0))
    visited[baby_x][baby_y] = True
    while find:
        now_x, now_y, now_t = find.popleft()
        for i in range(4): 
            if 0 <= now_x+dx[i] < N and 0 <= now_y+dy[i] < N:
                next_x, next_y = now_x+dx[i], now_y+dy[i]
                if area[next_x][next_y] <= baby_shark and not visited[next_x][next_y]:                    
                    if 0 < area[next_x][next_y] < baby_shark:
                        if_fish = True
                        fish_list.append((next_x, next_y, now_t+1))
                    visited[next_x][next_y] = True
                    find.append((next_x, next_y, now_t+1))
        if if_fish and (not find or now_t + 1 == find[0][2]):
            fish_list.sort()
            next_x, next_y, next_t = fish_list[0]
            time += next_t
            area[next_x][next_y] = 0
            baby_x, baby_y = next_x, next_y
            cnt += 1
            if cnt == baby_shark:
                cnt, baby_shark = 0, baby_shark + 1
            break
print(time)