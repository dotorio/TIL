import sys
sys.stdin = open('input.txt')

T = int(input())
for case in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    word_cnt = 0
    for i in range(N - K + 1):
        k = i
        for j in range(N):
            if 0 <= k-1 and arr[k-1][j] == 1:
                continue
            word_length = 0
            while k <= N - 1 and arr[k][j] == 1:
                word_length += 1
                k = k + 1
            if word_length == K:
                word_cnt += 1
            k = i
    for i in range(N - K + 1):
        k = i
        for j in range(N):
            if 0 <= k-1 and arr[j][k-1] == 1:
                continue
            word_length = 0
            while k <= N - 1 and arr[j][k] == 1:
                word_length += 1
                k = k + 1
            if word_length == K:
                word_cnt += 1
            k = i
    print(f'#{case} {word_cnt}')