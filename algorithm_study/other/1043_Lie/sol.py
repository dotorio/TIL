import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
member = [True]*N
can_lie_party = [True]*M
lie_cnt, *lie_mem = map(int, input().split())
parties = dict()
mem_to_party = dict()
for i in range(M):
    par_cnt, *party = map(int, input().split())
    parties[i] = party
max_party = M
while lie_mem:
    now_mem = lie_mem.pop()
    member[now_mem] = False
