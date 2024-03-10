import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque

node_cnt = int(input())
parent = [0]*(node_cnt-1)
con = deque()
for _ in range(node_cnt-1):
    a, b = map(int, input().split())
    if a == 1:
        parent[b-2] = 1
    elif b == 1:
        parent[a-2] = 1
    elif parent[a-2]:
        parent[b-2] = a
    elif parent[b-2]:
        parent[a-2] = b
    else:
        con.append([a,b])
    
while 0 in parent:
    now = con.popleft()   
    if parent[now[0]-2]:
        parent[now[1]-2] = now[0]
    elif parent[now[1]-2]:
        parent[now[0]-2] = now[1]
    else:
        con.append(now)
for i in parent:
    print(i)