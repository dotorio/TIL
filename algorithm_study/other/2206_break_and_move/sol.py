import sys
sys.stdin = open('input.txt')

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def go(queue):
    arrive = False
    while queue:
        x, y, cnt, can_break = queue.popleft()
        

N, M = map(int, input().split())
miro = [list(input()) for _ in range(N)]
queue = deque()
queue.append((0,0,1,True))
go(queue)