import sys
sys.stdin = open('sample_input.txt')

T = int(input())
# 테스트 개수를 받는다
for tc in range(1, T+1):
# 각 테스트마다
    V, E = map(int, input().split())
    # 노드의 개수와 간선의 개수를 받는다
    graph = {}
    # 그래프 형태를 나타낼 딕셔너리를 만든다
    for i in range(1, V+1):
        graph[i] = list()
        # 노드의 개수만큼 딕셔너리에
        # 노드 번호: [] 형태로 넣는다
    for i in range(E):
        A, B = map(int, input().split())
        graph[A].append(B)
        # 간선의 개수만큼 간선을 받아서
        # 딕셔너리에 넣는다
    S, G = map(int, input().split())
    # 시작 노드와 도착 노드를 받는다
    result = False
    # 경로가 있다면 result를 True로 바꿀 것이다
    need_visited, visited = list(), list()
    # 방문할 곳, 방문한 곳을 각각 리스트로 만든다
    need_visited.append(S)
    # 방문할 곳 리스트에 시작 노드를 넣는다
    while need_visited:
    # 방문할 곳이 없을 때까지 반복한다
        node = need_visited.pop()
        # 방문할 곳 스택 마지막에 넣은 노드를 빼낸다
        if node == G:
            # 만약 노드가 도착 노드라면
            result = True
            # 경로가 있는 것이므로 True로 바꾸고
            break
            # 즉각 멈춰라
        if node not in visited:
        # 만약 노드가 방문한 곳 리스트에 없다면
            visited.append(node)
            # 방문한 곳 리스트에 넣고
            need_visited.extend(graph[node])
            # 노드에 연결된 노드들을 방문할 곳 리스트에 넣는다
    if result == True:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')
        # 반복문을 모두 돌았을 때
        # 경로가 있다면 1, 없다면 0을 출력한다