import sys
sys.stdin = open('input.txt')

T = int(input())
for case in range(1, T+1):
    A = input()
    # if A == A[::-1]:
    #     print(f'#{case} 1')
    # else:
    #     print(f'#{case} 0')
    C = list(A)
    for i in range(int(len(C)/2)):
        C[i], C[len(C)-1-i] = C[len(C)-1-i], C[i]
    if A == ''.join(C):
        print(f'#{case} 1')
    else:
        print(f'#{case} 0')