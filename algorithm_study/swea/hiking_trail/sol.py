import sys
sys.stdin = open('input.txt')

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def find(i, j, num, cut):
    global max_way
    result = False
    for k in range(4):
        if 0<=i+dx[k]<N and 0<=j+dy[k]<N and not visit[i+dx[k]][j+dy[k]]:
            new_i, new_j = i+dx[k], j+dy[k]
            if MAP[i][j] > MAP[new_i][new_j]:                
                visit[new_i][new_j] = num+1
                find(new_i, new_j, num+1, cut)
                result = True
                visit[new_i][new_j] = 0
            elif cut and MAP[new_i][new_j]-K < MAP[i][j] <= MAP[new_i][new_j]:    
                ori = MAP[new_i][new_j]
                MAP[new_i][new_j] = MAP[i][j]-1
                cut = False
                visit[new_i][new_j] = num+1
                find(new_i, new_j, num+1, cut)
                result, cut = True, True
                MAP[new_i][new_j] = ori
                visit[new_i][new_j] = 0
    if not result:
        max_way = max(max_way, num)

for tc in range(1, int(input())+1):
    N, K = map(int, input().split())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    top_loc = []
    max_hei = 1
    for i in range(N):
        for j in range(N):
            if max_hei < MAP[i][j]:
                max_hei = MAP[i][j]
                top_loc = [[i, j]]
            elif max_hei == MAP[i][j]:
                top_loc.append([i, j])
    max_way = 1
    for i, j in top_loc:
        visit = [[0]*N for _ in range(N)]
        visit[i][j] = 1
        find(i, j, 1, True)
    print(f'#{tc} {max_way}')