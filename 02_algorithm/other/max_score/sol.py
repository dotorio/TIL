import sys
sys.stdin = open('input.txt')

for tc in range(int(input())):
    N, K = map(int, input().split())
    sc = sorted(list(map(int, input().split())), reverse = True)
    print(f'#{tc+1} {sum(sc[:K])}')