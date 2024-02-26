import sys
sys.stdin = open('input.txt')

T = int(input())
tree = [[] for _ in range(T+1)]
max_sum = 0
for _ in range(T):
    connect = list(map(int, input().split()))
    i = 0
    j = 1
    while connect[j] != -1:
        tree[connect[i]].append([connect[j], connect[j+1]])
        j += 2
for i in range(1, T):
    need_visited = list(range(i+1, T+1))
    stack = [tree[connect[i]]]
    
