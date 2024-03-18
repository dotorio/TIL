import sys
sys.stdin = open('input.txt')

N, K = map(int, input().split())
product = []
for _ in range(N):
    product.append(tuple(map(int, input().split())))
dp = [0] * (K+1)
for item in product:
    w,v = item
    for i in range(K,w-1,-1):
        dp[i] = max(dp[i],dp[i-w]+v)
print(dp[-1])