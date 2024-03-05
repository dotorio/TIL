import sys
sys.stdin = open('input.txt')
from collections import deque

def go(q, l, v):
    global result
    # 큐가 빌 때까지 반복
    while q:
        # 맨 앞의 좌표를 빼내서
        y, x = q.popleft()
        # 보석이 있는 좌표라면 
        if MAP[y][x] == 3:
            # result를 True로 바꾸고 return
            result = True
            return
        # 오른쪽의 좌표를 갈 수 있고 방문한 적 없다면
        if x+1<M and MAP[y][x+1] and not v[y][x+1]:
            # 방문을 표시하고 큐 안에 넣는다
            v[y][x+1] = 1
            q.append([y, x+1])
        # 왼쪽의 좌표를 갈 수 있고 방문한 적 없다면
        if x-1>=0 and MAP[y][x-1] and not v[y][x-1]:
            # 방문을 표시하고 큐 안에 넣는다
            v[y][x-1] = 1
            q.append([y, x-1])
        # 리미트만큼 위아래로 움직여본다
        for i in range(1, l+1):
            # 위쪽의 좌표를 갈 수 있고 방문한 적 없다면
            if y+i<N and MAP[y+i][x] and not v[y+i][x]:
                # 방문을 표시하고 큐 안에 넣는다
                v[y+i][x] = 1
                q.append([y+i, x])
            # 아랫쪽의 좌표를 갈 수 있고 방문한 적 없다면
            if y-i>=0 and MAP[y-i][x] and not v[y-i][x]:
                # 방문을 표시하고 큐 안에 넣는다
                v[y-i][x] = 1
                q.append([y-i, x])
N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
# 시작 위치를 찾아 변수에 저장해둔다
for i in range(N):
    for j in range(M):
        if MAP[i][j] == 2:
            start_y, start_x = i, j
# 보석을 찾으면 result를 True로 변경할 것이다
result = False
# 최소 리미트를 0으로 시작
limit = 0
# result가 True로 바뀔 때까지 반복
while not result:
    # 리미트를 1 올린다
    limit += 1
    # 방문한 곳을 표시할 리스트를 만들고 시작위치를 1로 바꾼다
    visited = [[0]*M for _ in range(N)]
    visited[start_y][start_x] = 1
    # 큐 안에 시작 위치를 넣고 함수 호출
    queue = deque([[start_y, start_x]])
    go(queue, limit, visited)
# 최소 리미트를 출력
print(limit)