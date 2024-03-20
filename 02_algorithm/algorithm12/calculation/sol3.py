import sys
sys.stdin = open('input.txt')

def f(cnt, stack_N, visit_N, stack_M, visit_M):
    new_s_N = []
    while stack_N:
        now = stack_N.pop()
        new_ap = {now+1, now-1, now*2, now-10}
        for i in new_ap:
            if 0 < i <= 10**6 and i not in visit_N:
                if i in stack_M:
                    return cnt*2-1
                new_s_N.append(i)
                visit_N.add(i)
    new_s_M = []
    while stack_M:
        now = stack_M.pop()
        new_ap = {now-1, now+1, now+10}
        if not now % 2:
            new_ap.add(now//2)
        for i in new_ap:
            if 0 < i <= 10**6 and i not in visit_M:
                if i in new_s_N:
                    return cnt*2
                new_s_M.append(i)
                visit_M.add(i)
    return f(cnt+1, new_s_N, visit_N, new_s_M, visit_M)

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    print(f'#{tc} {f(1, [N], {N}, [M], {M})}')