def f(stack, cnt, visit):
    new_s = []
    while stack:
        now = stack.pop()
        new_ap = {now*2, int(str(now)+'1')}
        for i in new_ap:
            if i == B:
                return cnt+1
            if 0<i<=10**9 and i not in visit:
                new_s.append(i)
                visit.add(i)
        if not new_s:
            return -1
    return f(new_s, cnt+1, visit)
            
A, B = map(int, input().split())
print(f([A], 1, {A}))