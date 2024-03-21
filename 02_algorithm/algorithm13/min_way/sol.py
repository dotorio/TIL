import sys
sys.stdin = open('input.txt')
from heapq import heappush, heappop

# 다익스트라

def dijkstra():
    pq = []

    # 시작점의 weight, node 번호를 한 번에 저장
    heappush(pq, (0, 0))

    while pq:
        # 최단 거리 노드에 대한 정보
        dist, now = heappop(pq)

        # pq의 특성 때문에 더 긴거리가 미리 저장되어 있음
        # now 가 이미 처리된 노드라면 pass
        if distance[now] < dist:
            continue

        # now 에서 인접한 다른 노드 확인
        for to in graph[now]:
            next_dist = to[0]
            next_node = to[1]

            # 누적 거리 계산
            new_dist = dist + next_dist

            # 이미 더 짧은 거리로 간 경우 pass
            if new_dist >= distance[next_node]:
                continue

            distance[next_node] = new_dist # 누적 거리를 최단 거리로 갱신
            heappush(pq, (new_dist, next_node)) # next_node 의 인접 노드들을 pq에 추가


for tc in range(1, int(input())+1):
    INF = int(1e15)
    N, E = map(int, input().split())

    # 인접 리스트
    graph = [[] for _ in range(N+1)]
    # 누적 거리를 저장할 변수
    distance = [INF] * (N+1)
    # 간선 정보 저장
    for _ in range(E):
        s, e, w = map(int, input().split())
        # graph[3] = [[4, 31]]
        graph[s].append([w, e])
    dijkstra()
    print(f'#{tc} {distance[N]}')

