import sys
sys.stdin = open('input.txt')
from collections import deque

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    city = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            
