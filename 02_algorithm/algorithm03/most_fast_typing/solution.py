import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for case in range(1, T+1):
    A, B = map(str, input().split())
    cnt = 0
    i = 0

    while i <= len(A)-1:
        if A[i:i+len(B)] == B:
            cnt += 1
            i += len(B)
        else:
            i += 1
            cnt += 1
    print(f'#{case} {cnt}')
