import sys
sys.stdin = open('input.txt')

def f(A,B):
    max_sum = 0
    for j in range(len(B) - len(A) + 1):
        sum = 0
        for i in range(len(A)):                
            sum += A[i] * B[i+j]
        max_sum = max(max_sum, sum)
    return max_sum
        
for tc in range(int(input())):
    N, M = map(int, input().split())
    seq1 = list(map(int, input().split()))
    seq2 = list(map(int, input().split()))
    if N <= M:
        print(f'#{tc+1} {f(seq1, seq2)}')
    else:
        print(f'#{tc+1} {f(seq2, seq1)}')