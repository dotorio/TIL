import sys
sys.stdin = open('input.txt')

def f(i, j, cnt, bnf):
    global max_bnf, max_now
    if cnt == 2:
        max_bnf = max(bnf, max_bnf)
        return
    if i == N:
        return
    if j+M-1 < N:
        f(i, j+1, cnt, bnf)
        max_now = 0
        g(hive[i][j:j+M], 0, 0, 0)
        if j+M < N:
            f(i, j+M, cnt+1, bnf + max_now)
        else:
            f(i+1, 0, cnt+1, bnf + max_now)
    else:
        f(i+1, 0, cnt, bnf)

def g(arr, i, can_clt, bnf_now):
    global max_now
    if i == M:
        max_now = max(max_now, bnf_now)
        return
    if can_clt + arr[i] <= C:
        g(arr, i+1, can_clt + arr[i], bnf_now + arr[i]**2)
    return g(arr, i+1, can_clt, bnf_now)

for tc in range(1, int(input())+1):
    N, M, C = map(int, input().split())
    hive = [list(map(int, input().split())) for _ in range(N)]
    max_bnf= 0
    f(0, 0, 0, 0)
    print(f'#{tc} {max_bnf}')