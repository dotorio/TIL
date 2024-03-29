from itertools import combinations
N, M = map(int, input().split())
a = list(combinations(list(range(1, N+1)), M))
for i in a:
    print(*i)