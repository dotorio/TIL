import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
listen = set()
see = set()
for _ in range(N):
    listen.add(input())
for _ in range(M):
    see.add(input())
new = list(listen & see)
print(len(new))
new.sort()
for i in new:
    print(i)

