import sys
sys.stdin = open('input.txt')

# i, j는 현재 좌표이고 base는 기준 높이
# equal은 지나오면서 base와 같은 높이였던 좌표 개수
# dir은 방향(r은 오른쪽, d는 아랫쪽)
def f(i, j, base, equal, dir):
    global con
    # 해당 행 or 열 끝까지 오는데 성공했다면
    if i == N or j == N:
        # 활주로를 1 더하고 리턴
        con += 1
        return
    # 현재 높이가 기준 높이와 같다면
    if MAP[i][j] == base:
        # 방향에 맞추어서 다음 함수로 순회
        if dir == 'r':
            return f(i, j+1, base, equal+1, dir)
        else:
            return f(i+1, j, base, equal+1, dir)
    # 현재 높이가 기준 높이보다 1 낮다면
    if MAP[i][j] == base-1:
        # 경사로의 길이만큼 현재 높이가 유지되는지
        for k in range(1, X):
            # 방향에 맞추어서 조사한다
            if dir == 'r':
                if j+k >= N or MAP[i][j] != MAP[i][j+k]:
                    return
            else:
                if i+k >= N or MAP[i][j] != MAP[i+k][j]:
                    return
        # 유지되었다면 방향에 맞추어서 다음 함수로 순회
        if dir == 'r':
            return f(i, j+X, MAP[i][j], 0, dir)
        else:
            return f(i+X, j, MAP[i][j], 0, dir)
    # 현재 높이가 기준 높이보다 1 높다면
    if MAP[i][j] == base+1:
        # 지나오면서 경사로를 만들만큼의
        # 충분한 거리가 없다면 리턴
        if equal < X:
            return
        # 충분한 거리가 있다면
        # 방향에 맞추어서 다음 함수로 순회
        else:
            if dir == 'r':
                return f(i, j+1, MAP[i][j], 1, dir)
            else:
                return f(i+1, j, MAP[i][j], 1, dir)
    # 현재 높이와 기준 높이가 2 이상 차이나면 리턴
    else:
        return


for tc in range(1, int(input())+1):
    N, X = map(int, input().split())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    # 활주로의 수
    con = 0
    # 가로 순회
    for i in range(N):
        f(i, 1, MAP[i][0], 1, 'r')
    # 세로 순회
    for j in range(N):
        f(1, j, MAP[0][j], 1, 'd')
    print(f'#{tc} {con}')
        