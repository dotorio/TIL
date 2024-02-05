import sys
sys.stdin = open('input.txt')

T = int(input())
for case in range(1, T+1):
    A = input()
    if A == A[::-1]:
        print(f'#{case} 1')
    else:
        print(f'#{case} 0')