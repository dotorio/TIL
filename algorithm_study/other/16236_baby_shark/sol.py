import sys
sys.stdin = open('input.txt')

from collections import deque

# 4방향을 지정
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

N = int(input())
area = [list(map(int, input().split())) for _ in range(N)]

# if fish = 먹을 수 있는 물고기를 발견했는가
# time = 마지막에 출력할 시간
# baby_shark = 현재 아기 상어의 크기
# cnt = 상어가 먹은 물고기 수
if_fish, time, baby_shark, cnt = False, 0, 2, 0

# 아기 상어의 위치를 찾아서 변수에 저장
for i in range(N):
    for j in range(N):
        if area[i][j]:
            if area[i][j] == 9:
                baby_x, baby_y = i, j
                area[i][j] = 0
            else:
                if_fish = True

# 물고기를 먹을 수 없을 때까지 반복
while if_fish:

    # fish_list = 먹을 수 있는 물고기들 중 가장 가까이 있는 물고기들의 좌표 리스트
    if_fish, fish_list = False, []
    visited = [[False]*N for _ in range(N)]
    min_dis = N**2

    # find 큐를 만들어서 bfs 시작
    find = deque()
    find.append((baby_x, baby_y, 0))
    visited[baby_x][baby_y] = True
    while find:
        now_x, now_y, now_t = find.popleft()
        for i in range(4): 

            # 4방향에서 갈 수 있는 위치이면 작업 시작
            if 0 <= now_x+dx[i] < N and 0 <= now_y+dy[i] < N:
                next_x, next_y = now_x+dx[i], now_y+dy[i]
                if area[next_x][next_y] <= baby_shark and not visited[next_x][next_y]:                    
                    
                    # 먹을 수 있는 물고기이면 if_fish를 True로 바꾸고
                    # fish_list에 좌표를 넣는다
                    if 0 < area[next_x][next_y] < baby_shark:
                        if_fish = True
                        fish_list.append((next_x, next_y, now_t+1))
                    visited[next_x][next_y] = True
                    find.append((next_x, next_y, now_t+1))
        
        # 먹을 수 있는 물고기를 발견했고 해당 거리까지 모두 순회했다면
        if if_fish and (not find or now_t + 1 == find[0][2]):

            # 가장 조건에 맞는 물고기를 찾아서
            fish_list.sort()
            next_x, next_y, next_t = fish_list[0]

            # time을 더해주고 area를 바꾸고 
            time += next_t
            area[next_x][next_y] = 0

            # 아기 상어의 위치를 바꾸고 먹은 물고기 수를 1 더한다
            baby_x, baby_y = next_x, next_y
            cnt += 1

            # 자기 크기만큼 먹었다면 크기를 1 키우고 먹은 물고기 수를 초기화
            if cnt == baby_shark:
                cnt, baby_shark = 0, baby_shark + 1
            break

# 마지막에 완성된 time을 출력
print(time)