import sys
sys.stdin = open('input.txt')

def DFS(A):
    while A:
        now = A.pop()
        if now == 99:
            return 1
        if now in visited:
            continue
        else:
            visited.append(now)
            stack.extend(graph[now])
    return 0

for _ in range(10):
    tc, way_cnt = map(int, input().split())
    ways = list(map(int, input().split()))
    graph = [[] for _ in range(100)]
    for i in range(way_cnt):
        graph[ways[2*i]].append(ways[2*i+1])
    stack = [0]
    visited = []
    print(f'#{tc} {DFS(stack)}')
