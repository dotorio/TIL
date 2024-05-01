import sys
sys.stdin = open('input.txt')

# 우선순위 큐 사용을 위해 힙을 사용한다
from heapq import heappop, heappush

# 4방향 설정
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    mt = [list(map(int, input().split())) for _ in range(N)]

    # 터널의 시작, 끝, 소모연료량을 표시할 리스트 3개    
    tn_s, tn_e, tn_c = [], [], []

    # 터널의 정보를 받아서 넣는다
    for _ in range(M):
        Ay, Ax, By, Bx, C = map(int, input().split())
        tn_s.append((Ay-1, Ax-1))
        tn_e.append((By-1, Bx-1))
        tn_c.append(C)

    # 우선순위 큐를 만든다
    pq = []

    # 방문을 표시할 리스트
    visited = [[False]*N for _ in range(N)]

    # 누적 연료와 시작 y, x 좌표를 우선순위 큐에 넣는다
    heappush(pq, (0, 0, 0))

    # 도착점에 갈때까지 반복
    while pq:
        now_c, now_y, now_x = heappop(pq)

        # 이전에 방문한 곳이라면 다음 좌표로 컨티뉴
        if visited[now_y][now_x]:
            continue

        # 도착점에 도착했다면 누적 연료를 출력하고 종료
        if (now_y, now_x) == (N-1, N-1):
            print(f'#{tc} {now_c}')
            break

        # 도착점이 아니라면 방문을 표시
        visited[now_y][now_x] = True

        # 4방향을 돌며 갈 수 있는 곳이고 방문하지 않은 곳이면 간다
        for i in range(4):
            n_y, n_x = now_y+dy[i], now_x+dx[i]
            if 0<=n_y<N and 0<=n_x<N and not visited[n_y][n_x]:
                if mt[n_y][n_x] > mt[now_y][now_x]:
                    n_c = now_c + 2*(mt[n_y][n_x]-mt[now_y][now_x])
                    heappush(pq, (n_c, n_y, n_x))
                elif mt[n_y][n_x] == mt[now_y][now_x]:
                    heappush(pq, (now_c+1, n_y, n_x))
                else:
                    heappush(pq, (now_c, n_y, n_x))

        # 현재 좌표가 터널의 시작점이거나 끝점이고 그 맞은편 좌표를
        # 아직 방문하지 않았다면 맞은편 좌표로 간다
        for i in range(M):
            if (now_y, now_x) == tn_s[i] and not visited[tn_e[i][0]][tn_e[i][1]]:
                heappush(pq, (now_c+tn_c[i], tn_e[i][0], tn_e[i][1]))
            elif (now_y, now_x) == tn_e[i] and not visited[tn_s[i][0]][tn_s[i][1]]:
                heappush(pq, (now_c+tn_c[i], tn_s[i][0], tn_s[i][1]))