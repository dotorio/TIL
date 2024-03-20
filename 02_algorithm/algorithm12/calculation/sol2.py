import sys
sys.stdin = open('input.txt')

def cal(cnt, stack, visit):
    if len(stack) == 1 and stack[0] > N*10:
        if stack[0] % 2:
            visit.add(stack[0]-1)
            return cal(cnt+1, [stack[0]-1], visit)
        else:
            visit.add(stack[0]//2)
            return cal(cnt+1, [stack[0]//2], visit)
    new_s = []
    while stack:
        now = stack.pop()
        new_ap = [now-1, now+1, now+10]
        if not now % 2:
            new_ap.append(now//2)
        for i in new_ap:
            if i not in visit and 0<i<=10**6:
                if i == N:
                    return cnt
                new_s.append(i)
                visit.add(i)
    return cal(cnt+1, new_s, visit)

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    print(f'#{tc} {cal(1, [M], {M})}')