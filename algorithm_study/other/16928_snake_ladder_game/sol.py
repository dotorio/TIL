import sys
sys.stdin = open('input.txt')
from collections import deque
input = sys.stdin.readline

board = [0]*101
lad_sna = [0]*101
N, M = map(int, input().split())
for i in range(N+M):
    start, end = map(int, input().split())
    lad_sna[start] = end
queue = deque([[1]])
cnt = 0
result = False
while True:
    next = queue.pop()
    cnt += 1
    linked = set()
    while next:
        now = next.pop()
        for i in range(1, 7):
            jump = now + i
            if jump == 100:
                result = True
                print(cnt)
                break
            if lad_sna[jump] != 0:
                if board[lad_sna[jump]] == 0:
                    linked.add(lad_sna[jump])
                    board[lad_sna[jump]] = 1
                board[jump] = 1
            elif board[jump] == 0:
                linked.add(jump)
                board[jump] = 1
        if result == True:
            break
    if result == True:
        break
    if linked:
        queue.append(list(linked))
