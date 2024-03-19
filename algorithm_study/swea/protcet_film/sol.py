import sys
sys.stdin = open('input.txt')

def g(col, ctn, arr):
    for i in range(W):
        if not arr[i]:
            if film[col][i] == film[col-1][i]:
                ctn[i] += 1
                if ctn[i] == K:
                    arr[i] = True
            else:
                ctn[i] = 1

def f(col, ctn, med_cnt, arr):
    global min_med

    if False not in arr:
        min_med = min(min_med, med_cnt)
        return

    if K-min(ctn) > D-col:
        return

    if col == D or not min_med:
        return

    if col:
        org_ctn, org_arr = ctn[:], arr[:]
        g(col, ctn, arr)
        f(col+1, ctn, med_cnt, arr)
        
        film[col] = [0]*W
        ctn, arr = org_ctn[:], org_arr[:]
        g(col, ctn, arr)
        f(col+1, ctn, med_cnt+1, arr)

        film[col] = [1]*W
        ctn, arr = org_ctn[:], org_arr[:]
        g(col, ctn, arr)
        f(col+1, ctn, med_cnt+1, arr)

    else:
        f(1, ctn, 0, arr)
        film[col] = [0]*W
        f(1, ctn, 1, arr)
        film[col] = [1]*W
        f(1, ctn, 1, arr)

for tc in range(1, int(input())+1):
    D, W, K = map(int, input().split())
    film = [list(map(int, input().split())) for _ in range(D)]
    min_med, ctn, arr = K, [1]*W, [False]*W
    if K == 1:
        print(f'#{tc} 0')
    else:
        f(0, ctn, 0, arr)
        print(f'#{tc} {min_med}')