import sys
sys.stdin = open('input.txt')
from collections import deque
input = sys.stdin.readline
N, K, T = map(int, input().split())
ori = T
shark = sorted(deque(map(int, input().split())))
max_shark = shark[-1]
eat = 0
result = False
while shark:
    now = shark.popleft()
    if not shark:
        if now < T:
            T += now
            result = True
            print(T)
            break
    if now < T <= shark[0]:
        T += now
        eat += 1
    else:
        shark.append(now)
    if eat == K:
        break
if ori == T or eat == K or not result:
    print(T)
else:
    while eat != K and later:
        now = later.pop()
        T += now
        eat += 1

    print(T)