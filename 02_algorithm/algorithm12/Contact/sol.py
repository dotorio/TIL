import sys
sys.stdin = open('input.txt')
from collections import deque

for tc in range(1, 11):
    d_len, start = map(int, input().split())
    data = list(map(int, input().split()))
    call = {i:[] for i in range(1, 101)}
    visit = [False]*101
    for i in range(len(data)//2):
        call[data[2*i-1]].append(data[2*i])
    queue = deque([start, 1])
    max_rank, last_max_num = 0, 0
    while queue:
        now = queue.popleft()
        if not visit[now]:
            visit[now] = True
            
            max_num = max(now, max_num)
            queue.extend(call[now])
    print(f'#{tc} {max_num}')