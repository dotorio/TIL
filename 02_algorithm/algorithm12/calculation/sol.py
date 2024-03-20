import sys
sys.stdin = open('input.txt')

def cal(stack, cnt, visit):
    if max(stack) < M//10:
        visit.add(max(stack)*2)
        return cal([max(stack)*2], cnt+1, visit)
    new_s = []
    while stack:
        now = stack.pop()
        new_ap = {now+1, now-1, now*2, now-10}
        if M in new_ap:
            return cnt
        for i in new_ap:
            if 0 < i <= 10**6 and i not in visit:
                new_s.append(i)
                visit.add(i)
    return cal(new_s, cnt+1, visit)

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    print(f'#{tc} {cal([N], 1, {N})}')