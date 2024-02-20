import sys
sys.stdin = open('input.txt')

for tc in range(int(input())):
    N = int(input())
    farm = [list(map(int, input())) for _ in range(N)]
    profit = sum(farm[N//2])
    for i in range(N//2):
        profit += sum(farm[i][N//2 - i : N//2 + i + 1])
        profit += sum(farm[N-1-i][N//2 - i : N//2 + i + 1])
    print(f'#{tc+1} {profit}')