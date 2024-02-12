import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline

N, K = map(int, input().split())
coins = list(int(input()) for _ in range(N))
sum = 0
cnt = 0
for i in range(1, N+1):
    coin = coins[-i]
    while sum + coin <= K:
        sum += coin
        cnt += 1
    if sum == K:
        break
print(cnt)