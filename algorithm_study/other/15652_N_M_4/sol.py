from itertools import combinations_with_replacement

N, M = map(int, input().split())

answer = combinations_with_replacement(list(range(1, N+1)), M)
for i in answer:
    print(*i)