import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
stack = []
for _ in range(N):
    com = list(map(int, input().split()))
    if com[0] == 1:
        stack.append(com[1])
    elif com[0] == 2:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif com[0] == 3:
        print(len(stack))
    elif com[0] == 4:
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    else:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
