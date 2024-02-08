import sys
sys.stdin = open('input.txt')

def DFS(start):
    visited[start] = 1
    print(start, end=' ') 
    
    for next in range(1, V+1):
        if visited[next] == 0 and adj[start][next] == 1:
            DFS(next)


V, E = map(int, input().split())
arr = list(map(int, input().split()))
visited = [0] * (V+1)
# 인접 행렬
adj = [[0] * (V+1) for _ in range(V+1)]
for i in range(E):
    # 무방향 그래프니까 반대로도 넣자
    adj[arr[i*2]][arr[i*2+1]] = 1
    adj[arr[i*2+1]][arr[i*2]] = 1
DFS(1)