import sys
sys.stdin = open('input.txt')

std = {0 : [0]*6, 1 : [0]*6}
room = 0
N, K = map(int, input().split())
for i in range(N):
    S, Y = map(int, input().split())
    std[S][Y-1] += 1
for i in std:
    for j in range(6):
        if not std[i][j]:
            continue
        elif std[i][j] % K == 0:
            room += std[i][j] // K
        else:
            room += std[i][j] // K + 1
print(room)
