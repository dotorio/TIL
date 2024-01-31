import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for case in range(1, T + 1):
    N, Q = map(int, input().split())
    arr = [0] * N
    for change in range(1, Q + 1):
        start, end = map(int, input().split())
        for i in range(start - 1, end):
            arr[i] = change
    print(f'#{case} {" ".join(map(str, arr))}')