import sys
sys.stdin = open('input.txt')

pc_cnt = int(input())
net = {}
for i in range(1, pc_cnt+1):
    net[i] = []
con = int(input())
for _ in range(con):
    a, b = map(int, input().split())
    net[a].append(b)
    net[b].append(a)
visit = [0]*(pc_cnt+1)
visit[1] = 1
stack = net[1][:]
virus = 0
while stack:
    now = stack.pop()
    if visit[now]:
        continue
    else:
        visit[now] = 1
        stack.extend(net[now])
        virus += 1
print(virus)