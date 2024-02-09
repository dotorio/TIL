import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
queue = []
for _ in range(N):
    com = list(input().split())
    if com[0] == 'push':
        queue.append(int(com[1]))
    elif com[0] == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.pop(0))
    elif com[0] == 'size':
        print(len(queue))
    elif com[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif com[0] == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    else:
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
