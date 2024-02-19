import sys
sys.stdin = open('input.txt')
from queue import PriorityQueue

T = int(input())
for _ in range(T):
    k = int(input())
    que1 = PriorityQueue()
    que2 = PriorityQueue()
    cnt = 0
    for _ in range(k):
        A, B = input().split()
        if A == 'I':
            cnt += 1
            que1.put(int(B))
            que2.put(-(int(B)))
        else:
            if cnt == 0:
                continue
            if B == '1':
                cnt -= 1
                que2.get()
            else:
                cnt -= 1
                que1.get()
            
    if cnt == 0:
        print('EMPTY')
    else:
        print(-(que2.get()), que1.get())

