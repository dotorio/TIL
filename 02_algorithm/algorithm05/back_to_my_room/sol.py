import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    rooms = []
    for _ in range(N):
        rooms.append(list(map(int, input().split())))
    visited = [0]*201
    for i in rooms:
        start = (min(i)+1)//2
        end = (max(i)+1)//2
        for j in range(start, end+1):
            visited[j] += 1
    print(f'#{tc} {max(visited)}')