import sys
sys.stdin = open('input.txt')
from heapq import heappop, heappush

def f(start, end):
    pq = []
    distance = [INF]*(N+1)
    heappush(pq, (0, start))
    while pq:
        time, now = heappop(pq)
        if now == end:
            return time
        if distance[now] < time:
            continue
        for i in graph[now]:
            new_time = time + i[1]
            if new_time < distance[i[0]]:
                distance[i[0]] = new_time
                heappush(pq, (new_time, i[0]))

INF = int(1e9)        
for tc in range(1, int(input())+1):
    N, M, X = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        x, y, c = map(int, input().split())
        graph[x].append((y, c))
    max_time = 0
    for i in range(1, N+1):
        if i != X:
            max_time = max(max_time, (f(i, X)+f(X, i)))
    print(f'#{tc} {max_time}')