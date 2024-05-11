# 4방향 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 마지막에 출력할 시간을 0으로 설정
time = 0

# 치즈가 모두 녹을 때까지 반복
while True:
    
    # 치즈 외부 공기가 있는 곳을 True로 바꿀 check_arr
    check_arr = [[False]*M for _ in range(N)]
    stack = [(0, 0)]
    check_arr[0][0] = True
    while stack:
        i, j = stack.pop()
        for k in range(4):
            if 0<=i+dx[k]<N and 0<=j+dy[k]<M:
                if not check_arr[i+dx[k]][j+dy[k]] and not arr[i+dx[k]][j+dy[k]]:
                    stack.append((i+dx[k], j+dy[k]))
                    check_arr[i+dx[k]][j+dy[k]] = True
                    
    # 녹여야할 좌표를 넣을 melt
    melt = []
    for i in range(N):
        for j in range(M):
            if arr[i][j]:
                cnt = 0
                for k in range(4):
                    if not arr[i+dx[k]][j+dy[k]] and check_arr[i+dx[k]][j+dy[k]]:
                        cnt += 1
                if cnt >= 2:
                    melt.append((i , j))
                    
    # 녹일 좌표가 없다면 시간을 출력하고 break
    if not melt:
        print(time)
        break
    
    # 녹일 좌표가 있다면 녹이고 다음 순회로
    else:
        for i, j in melt:
            arr[i][j] = 0
    time += 1