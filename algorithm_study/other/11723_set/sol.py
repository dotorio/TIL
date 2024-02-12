import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

set = set()
M = int(input())
for _ in range(M):
    com = list(input().split())
    if com[0] == 'add':
        set.add(int(com[1]))
    elif com[0] == 'remove':
        if int(com[1]) not in set:
            continue
        else:
            set.remove(int(com[1]))
    elif com[0] == 'check':
        if int(com[1]) in set:
            print(1)
        else:
            print(0)
    elif com[0] == 'toggle':
        if int(com[1]) in set:
            set.remove(int(com[1]))
        else:
            set.add(int(com[1]))
    elif com[0] == 'all':
        set.update(list(range(1, 21)))
    else:
        set.clear()
