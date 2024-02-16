import sys
sys.stdin = open('input.txt')
from collections import deque

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    # 연결된 노드를 표시할 linked 리스트를 만든다
    linked = [[] for _ in range(V+1)]
    # 방문하면 거리를 할당할 visited 리스트를 만든다
    visited = [None]*(V+1)
    # 무방향 간선이므로 양쪽으로 append한다
    for _ in range(E):
        A, B = map(int, input().split())
        linked[A].append(B)
        linked[B].append(A)
    start, end = map(int, input().split())
    # 시작 노드를 넣은 큐를 만든다
    queue = deque([start])
    # 시작점의 거리는 0이다
    visited[start] = 0
    # 도착점을 찾으면 result를 True로 바꿀 것이다
    result = False
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 노드 하나를 빼서
        now = queue.popleft()
        # 그 노드로부터 연결된 노드들을 순회하며
        for i in linked[now]:
            # 연결된 노드가 도착점이 아니고 방문하지 않았다면
            if i != end and visited[i] == None:
                # 직전 거리에서 1 더한 값을 거리로 할당하고
                visited[i] = visited[now] + 1
                # 큐에 연결된 노드를 넣는다
                queue.append(i)
            # 연결된 노드가 도착점이라면 해당 거리를 출력하고 break
            elif i == end:
                result = True
                print(f'#{tc} {visited[now]+1}')
                break
        if result == True:
            break
    # 반복을 끝내도 도착하지 못했다면 0 출력
    if result == False:
        print(f'#{tc} 0')
