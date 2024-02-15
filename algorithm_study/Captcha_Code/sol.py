import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    sample = list(map(int, input().split()))
    passcode = list(map(int, input().split()))
    result, i, j = 0, 0, 0
    while i != len(sample):
        if sample[i] == passcode[j]:
            i += 1
            j += 1
            if j == len(passcode):
                result = 1
                break
        else:
            i += 1
    print(f'#{tc} {result}')