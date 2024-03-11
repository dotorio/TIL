import sys
sys.stdin = open('input.txt')

N = int(input())
tree = {}
for i in range(1, N+1):
    tree[i] = []
for _ in range(N-1):
    a, b =map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
parent = [0] * (N+1)
stack = []
for i in tree[1]:
    stack.append([1,i])
parent[1] = 1
while stack:
    par, son = stack.pop()
    if not parent[son]:
        parent[son] = par
        for i in tree[son]:
            stack.append([son, i])
for i in range(2, N+1):
    print(parent[i])