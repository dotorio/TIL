import sys
sys.stdin = open('input.txt')
from heapq import heappush, heappop

def prim(start):

    # 힙으로 사용할 pq
    pq = []

    # 방문한 곳을 표시할 visited
    visited = [0] * (V+1)

    # 최소 가중치 합을 0으로 설정한다
    sum_weight = 0

    # 힙에 (0, 최초 노드)를 넣는다
    heappush(pq, (0, start))

    # 힙이 없어질 때까지 순회
    while pq:

        # 현재 가장 작은 가중치의 합과 그 노드를 힙에서 빼낸다
        weight, now = heappop(pq)

        # 방문 했다면 다음 순회로
        if visited[now]:
            continue

        # 방문 처리
        visited[now] = 1

        # 최소 가중치 추가
        sum_weight += weight

        # 갈 수 있는 노드들을 보면서
        for to in range(V+1):

            # 갈 수 없거나 이미 방문했다면 continue
            if not graph[now][to] or visited[to]:
                continue
            
            # 갈 수 있다면 힙에 넣는다
            heappush(pq, (graph[now][to], to))
    
    # 마지막에 완성된 최소 가중치를 출력한다
    print(f'#{tc} {sum_weight}')
    

for tc in range(1, int(input())+1):
    V, E = map(int, input().split())

    # 연결 정보를 저장할 그래프
    graph = [[0] * (V+1) for _ in range(V+1)]

    # 그래프를 완성한다
    for _ in range(E):
        start, end, weight = map(int, input().split())

        # 무방향 그래프이므로 둘 다 기록한다
        graph[start][end] = weight
        graph[end][start] = weight
    
    # 0번 노드를 출발점으로 시작한다
    # 노드 번호는 몇번으로 시작하든 상관없다
    prim(0)