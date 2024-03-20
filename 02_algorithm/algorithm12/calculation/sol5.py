import sys
sys.stdin = open('input.txt')
from collections import deque

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    visit = [False]*(10**6+1)
    queue = deque([[M , 0]])
    while queue:
        num, cnt = queue.popleft()
        if visit[num]:
            continue
        if num == N:
            print(f'#{tc} {cnt}')
            break
        visit[num] = True
        if num+1 <= 10**6:
            queue.append([num+1, cnt+1])
        if 0< num-1:
            queue.append([num-1, cnt+1])
        if num+10 <= 10**6:
            queue.append([num+10, cnt+1])
        if 1< num and not num%2 :
            queue.append([num//2, cnt+1])