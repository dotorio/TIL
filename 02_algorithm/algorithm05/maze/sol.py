import sys
sys.stdin = open('input.txt')

# 테스트 개수를 받는다
T = int(input())
# 이후 4방향을 체크할 리스트들을 만든다
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# 각 테스트마다
for tc in range(1, T+1):
    # 미로의 크기를 받는다
    N = int(input())
    # 미로를 리스트 형태로 입력받는다
    maze = [list(map(int, input())) for _ in range(N)]
    # 방문을 표시할 visited 리스트를 만든다
    visited = [[0]*N for _ in range(N)]
    # 미로 안 2를 찾아 좌표를 변수에 저장한다
    for x in range(N-1, -1, -1):
        if 2 in maze[x]:
            now_x, now_y = x, maze[x].index(2)
            break
    # 스택을 만들고 출발 좌표를 넣는다
    stack = [[now_x, now_y]]
    # 출발 좌표는 방문했으므로 visited를 변경한다
    visited[now_x][now_y] = 1
    # 도착에 성공한다면 결과를 1로 바꿀 것이다
    result = 0
    # 스택이 빌 때까지 반복한다
    while stack:
        # 현재 좌표는 스택에 저장된 마지막 좌표
        now = stack[-1]
        # 4방향을 순회하면서
        for i in range(4):
            next_x = now[0]+dx[i]
            next_y = now[1]+dy[i]
            # 그 방향의 좌표가 미로의 범위 내에 있으면 진행
            if 0 <= next_x < N and 0 <= next_y < N:
                # 만약 도착했다면
                if maze[next_x][next_y] == 3:
                    # 결과를 1로 바꾸고                    
                    result = 1
                    # 테케와 결과를 출력한다
                    print(f'#{tc} {result}')
                    # 그리고 즉각 종료
                    break
                # 만약 진행한 좌표값이 0이고 방문하지 않았다면
                elif maze[next_x][next_y] == 0 and visited[next_x][next_y] == 0:
                    # 이제 방문했으므로 visited를 변경해주고
                    visited[next_x][next_y] = 1
                    # 스택에 해당 좌표를 넣는다
                    stack.append([next_x, next_y])
                    # 스택이 변경되었으므로 4방향 순회를 종료한다
                    break
        # 만약 4방향을 모두 순회해도 갈수 있는 좌표가 없다면
        else:
            # 해당 좌표는 필요없으므로 없앤다
            stack.pop()
        # 만약 결과가 1이라면
        if result == 1:
            # 반복할 필요가 없으므로 종료
            break
    # 스택이 빌 때까지 반복해도 도착하지 못했다면
    if result == 0:
        # 테케와 결과를 출력한다
        print(f'#{tc} {result}')