import sys
sys.stdin = open('input.txt')
from collections import deque

# 4방향을 설정할 리스트를 만든다
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    # 미로를 돌며 2를 찾아 그 좌표를 변수에 할당한다
    for i in range(N):
        if 2 in maze[i]:
            start_x, start_y = i, maze[i].index(2)
    # 마지막에 출력할 길이는 반복문 안에서 1씩 더할 것이기에
    # 기본값을 -1로 시작한다
    cnt = -1
    # 도착점을 찾으면 result를 True로 바꿀 것이다
    result = False
    # 시작 좌표를 넣은 큐를 만든다
    queue = deque([[[start_x, start_y]]])
    # 큐가 빌 때까지 반복
    while queue:
        # 다음 좌표들을 불러와서
        next = queue.popleft()
        # 길이는 1 더하고
        cnt += 1
        # 연결된 좌표들을 저장할 linked 리스트를 만든다
        linked = []
        # 좌표들이 없어질 때까지 반복
        while next:
            # 좌표 하나를 빼서
            now = next.pop()
            # 4방향으로 보내서
            for i in range(4):
                around_x, around_y = now[0] + dx[i], now[1] + dy[i]
                # 그 좌표가 미로의 범위 안에 있고
                if 0 <= around_x < N and 0 <= around_y < N:
                    # 그 좌표가 갈수 있는 곳이라면
                    if maze[around_x][around_y] == 0:
                        # linked 리스트에 넣는다
                        linked.append([around_x, around_y])
                        # 방문한 곳을 또 갈 필요없으니 벽으로 바꾼다
                        maze[around_x][around_y] = 1
                    # 그 좌표가 도착점이라면 길이를 출력하고 break
                    elif maze[around_x][around_y] == 3:
                        result = True
                        print(f'#{tc} {cnt}')
                        break
            if result == True:
                break
        if result == True:
            break
        # 연결된 좌표가 있을 때에만 큐에 넣는다
        if linked != []:
            queue.append(linked)
    # 끝까지 도착하지 못하면 0 출력
    if result == False:
        print(f'#{tc} 0')