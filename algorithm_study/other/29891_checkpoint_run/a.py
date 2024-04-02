def f(idx, day, bnf):
    global max_bnf
    if day > n or idx == n:
        return
    max_bnf = max(max_bnf, bnf)
    day += work[idx][0]
    bnf += work[idx][1]
    idx += 1   
    f(idx, day, bnf)
    day -= work[idx-1][0]
    bnf -= work[idx-1][1]     
    f(idx, day, bnf)

n = int(input())
work = []
for _ in range(n):
    t, p = map(int, input().split())
    work.append((t, p))
max_bnf = 0
f(0, 0, 0)
print(max_bnf)