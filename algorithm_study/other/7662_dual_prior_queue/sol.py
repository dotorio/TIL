import sys
sys.stdin = open('input.txt')

import heapq

for T in range(int(input())):
    heap1 = []
    heap2 = []
    cnt = 0
    for k in range(int(input())):
        A, B = input().split()
        if A == 'I':
            heapq.heappush(heap1, int(B))
            heapq.heappush(heap2, -int(B))
            cnt += 1
        else:
            if cnt == 0:
                continue
            if B == '1':
                heapq.heappop(heap2)
                cnt -= 1
            else:
                heapq.heappop(heap1)
                cnt -= 1
    if cnt == 0:
        print('EMPTY')
    else:
        print(-(heapq.heappop(heap2)), heapq.heappop(heap1))