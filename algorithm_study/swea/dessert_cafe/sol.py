import sys
sys.stdin = open('input.txt')

dx = [-1, 1, 1, -1]
dy = [1, 1, -1, -1]

for tc in range(1, int(input())+1):
    N = int(input())
    loc = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N-2):
        for j in range(1, N-1):
            f(i, j)