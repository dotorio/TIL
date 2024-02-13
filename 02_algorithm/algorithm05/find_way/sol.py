import sys
sys.stdin = open('input.txt')

# 함수의 정의는 함수 호출 시에 올라와서 본다
def DFS(A):
    # 스택이 빌 때까지 반복
    while A:
        # 스택에 마지막에 넣은 노드를 빼내서
        now = A.pop()
        # 만약 그 노드가 도착점이라면
        if now == 99:
            # 1을 반환
            return 1
        # 만약 그 노드가 방문한 노드라면
        if now in visited:
            # 다음 반복으로 간다
            continue
        # 만약 그 노드가 방문하지 않은 노드라면
        else:
            # visited에 넣고
            visited.append(now)
            # 그래프 상에서 연결된 노드 전체를 스택에 넣는다
            stack.extend(graph[now])
    # 끝까지 반복해도 도착점에 도달하지 못하면 0을 반환
    return 0

# 테스트의 개수는 10개
for _ in range(10):
    # 각 테스트마다 테스트 번호와 길의 개수를 받는다
    tc, way_cnt = map(int, input().split())
    # 길들을 리스트에 담는다
    ways = list(map(int, input().split()))
    # 길의 방향을 표현할 리스트 모양의 그래프를 만든다
    graph = [[] for _ in range(100)]
    # 길의 방향을 그래프에 표현한다
    for i in range(way_cnt):
        graph[ways[2*i]].append(ways[2*i+1])
    # 첫 시작은 0에서 시작
    stack = [0]
    # 방문한 노드는 visited에 담을 것이다
    visited = []
    # DFS 함수에 따라 나온 결과를 테케와 함께 출력한다
    print(f'#{tc} {DFS(stack)}')
