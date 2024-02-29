import sys
sys.stdin = open('input.txt')
from collections import deque
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def grow(a):
    global cnt
    for i in range(4):
        if 0<=a[0]+dx[i]<N and 0<=a[1]+dy[i]<M:
            new_x, new_y = a[0]+dx[i], a[1]+dy[i]
            if tomato[new_x][new_y] == 0:
                tomato[new_x][new_y]  = a[2]+1
                queue.append((new_x, new_y, a[2]+1))
    
def find(a):
    max_grow = 0
    for j in range(N):
        for k in range(M):
            if a[j][k] > 0:
                max_grow = max(max_grow, a[j][k])
            elif a[j][k] == 0:
                return -1
    return max_grow

M, N= map(int, input().split())
tomato = [list(map(int, input().split())) for i in range(N)]
queue = deque()
result = False
for j in range(N):
    for k in range(M):
        if tomato[j][k] == 1:
            queue.append((j, k, 0))
        elif tomato[j][k] == 0:
            result = True

while queue:
    now = queue.popleft()
    grow(now)
if result:
    print(find(tomato))
else:
    print(0)