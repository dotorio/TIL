import sys
sys.stdin = open('input.txt')

def make_set(n):
    return [i for i in range(n)], [0 for _ in range(n)]

def find_set(x):
    if group[x] == x:
        return x
    return find_set(group[x])

def union(x, y):
    x = find_set(x)
    y = find_set(y)
    if x == y:
        return    
    if x < y:
        group[y] = x
    else:
        group[x] = y

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    paper = list(map(int, input().split()))
    group, rank = make_set(N+1)
    while paper:
        union(paper.pop(), paper.pop())
    g_num = set()
    for i in range(1, N+1):
        g_num.add(find_set(i))
    print(f'#{tc} {len(g_num)}')