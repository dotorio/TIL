import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    price = list(map(int, input().split()))
    profit = 0
    max_price = 0
    for i in range(N-1, -1, -1):
        if price[i] > max_price:
            max_price = price[i]
        profit += max_price - price[i]
    print(f'#{tc} {profit}')