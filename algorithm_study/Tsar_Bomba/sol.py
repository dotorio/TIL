import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, P = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_sum = 0
    for i in range(N):
        for j in range(N):
            sum = arr[i][j]
            for k in range(1, P+1):
                for dx, dy in [-1, 0], [1, 0], [0, -1], [0, 1]:
                    di = i + dx * k
                    dj = j + dy * k
                    if 0 <= di < N and 0 <= dj < N:
                        sum += arr[di][dj]
                if max_sum < sum:
                    max_sum = sum
    print(f'#{tc} {max_sum}')
