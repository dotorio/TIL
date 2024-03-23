import sys
sys.stdin = open('input.txt')
from heapq import heappush, heappop

for tc in range(1, int(input())+1):
    N = int(input())
    loc_x = list(map(int, input().split()))
    loc_y = list(map(int, input().split()))
    loc = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i != j:
                loc[i][j] = (loc_x[i]-loc_x[j])**2 + (loc_y[i]-loc_y[j])**2
    visit = [False]*N
    sum_tunnel = 0
    E = float(input())
    pq = []
    heappush(pq, (0, 0))
    while pq:
        tunnel, island= heappop(pq)
        if visit[island]:
            continue
        visit[island] = True
        sum_tunnel += tunnel
        if False not in visit:
            print(f'#{tc} {(sum_tunnel*E):.0f}')
            break
        for to in range(N):
            if not visit[to] and loc[island][to]:
                heappush(pq, (loc[island][to] ,to))
    