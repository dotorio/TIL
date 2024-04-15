import sys
sys.stdin = open('input.txt')

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def watch(x, y, dir):
    stack = []
    for i in dir:
        

N, M = map(int, input().split())
office = [list(map(int, input().split())) for _ in range(N)]
cctv = []
for i in range(N):
    for j in range(M):
        if office[i][j] == 5:
            watch(i, j, list(range(4)))