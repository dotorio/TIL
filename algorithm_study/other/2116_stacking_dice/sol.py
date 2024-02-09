import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
dices = [list(map(int, input().split())) for _ in range(N)]
max_sum = 0
for j in range(6):
    sum = 0
    for i in range(N):
        if j == 0:
            next = 5
        elif j in [1, 2]:
            next = j+2
        elif j in [3, 4]:
            next = j-2
        else:
            next = 0
        side = set(dices[i])
        side = side - {dices[i][j], dices[i][next]}
        sum += max(side)
        if i != N-1:
            j = dices[i+1].index(dices[i][next])
    if max_sum < sum:
        max_sum = sum
print(max_sum)

