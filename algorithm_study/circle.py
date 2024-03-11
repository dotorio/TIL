dx = [-1, 0]
dy = [0, 1]

r1, r2 = map(int, input().split())
visited = []
stack = [[r2, 0]]
answer = 0
while stack:
    x, y = stack.pop()
    if [x, y] not in visited:
        visited.append([x, y])
        answer += 1
        for i in range(2):
            if x+dx[i] != 0 and r1**2 <= (x+dx[i])**2 + (y+dy[i])**2 <= r2**2:
                stack.append([x+dx[i], y+dy[i]])   
print(answer*4)         