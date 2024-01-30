import sys
sys.stdin = open('sample_input.txt')

def cnt_c(loc, ch, k, num):
    for o in range(loc+1, len(ch)):
        if ch[o] - ch[loc] > k:
            num += 1
            loc = o-1
            return cnt_c(loc, ch, k, num)
        elif ch[o] - ch[loc] == k and N - ch[loc] != k:
            num += 1
            loc = o
            return cnt_c(loc, ch, k, num)

    return num

T = int(input())
for _ in range(T):
    K, N, M = map(int, input().split())
    charge = list(map(int, input().split()))
    d_charge = []
    for i in range(len(charge)-1):
        d_charge.append(charge[i+1] - charge[i])
    if K < max(d_charge):
        print(f'#{_+1} 0')
    else:
        c_number = 0
        charge = [0] + charge + [N]
        print(f'#{_+1} {cnt_c(0, charge, K, c_number)}')





