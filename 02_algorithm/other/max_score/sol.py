import sys
sys.stdin = open('input.txt')

for tc in range(int(input())):
    N, K = map(int, input().split())
    sc = sorted(list(map(int, input().split())), reverse = True)
    max_sc = 0
    for i in range(K):
        max_sc += sc[i]
    print(f'#{tc+1} {max_sc}')