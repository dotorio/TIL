import sys
sys.stdin = open('input.txt')
from heapq import heappush, heappop

# 4방향을 설정할 리스트
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def f(i, j):

    # 힙으로 사용할 pq
    pq = []

    # 방문을 표시할 visit
    visit = [[0]*N for _ in range(N)]

    # 힙에 현재 쓴 연료(0)와 첫 좌표를 넣는다
    heappush(pq, (0, (i, j)))

    while pq:
        fuel, (x, y) = heappop(pq)

        # 맨 오른쪽 아래 좌표를 만났다면
        if (x, y) == (N-1, N-1):

            # 현재 쓴 최소 연료를 출력하고 끝낸다
            print(f'#{tc} {fuel}')
            break

        # 방문 했다면 continue
        if visit[x][y]:
            continue

        # 방문 처리
        visit[x][y] = 1

        # 4방향에 대해서
        for k in range(4):

            # 갈 수 있다면
            if 0<=x+dx[k]<N and 0<=y+dy[k]<N:

                # 조건에 맞게 힙에 넣는다
                if height[x][y] >= height[x+dx[k]][y+dy[k]]:
                    heappush(pq, (fuel+1, (x+dx[k], y+dy[k])))
                else:
                    heappush(pq, (fuel + 1 + height[x+dx[k]][y+dy[k]] - height[x][y], (x+dx[k], y+dy[k])))
                
for tc in range(1, int(input())+1):
    N = int(input())
    height = [list(map(int, input().split())) for _ in range(N)]
    
    # 맨 왼쪽 위 좌표로 함수 시작
    f(0, 0)