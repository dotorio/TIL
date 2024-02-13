import sys
sys.stdin = open('input.txt')

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(10):
    tc = int(input())
    maze = [list(map(int, input())) for _ in range(16)]
    visited = [[0] * 16 for _ in range(16)]
    stack = []
    for x in range(16):
        if 2 in maze[x]:
            stack.append([x, maze[x].index(2)])
            break

    
    