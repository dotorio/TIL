import sys
sys.stdin = open('input.txt')
from collections import deque

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    time = deque(sorted(list(map(int, input().split()))))
    bread = 0
    result = True
    for i in range(max(time)+1):
        if i !=0 and i % M == 0:
            bread += K
        if i == time[0]:
            while len(time) != 0 and i == time[0]:
                if bread != 0:
                    bread -= 1
                    time.popleft()
                else:
                    result = False
                    print(f'#{tc} Impossible')
                    break
        if result == False:
            break
    if result == True:
        print(f'#{tc} Possible')