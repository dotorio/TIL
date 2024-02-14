import sys
sys.stdin = open('input.txt')

# 테스트의 개수를 받는다
T = int(input())
# 각 테스트마다
for tc in range(1, T+1):
    # 게임판의 크기를 받아서
    N = int(input())
    # 게임판을 리스트로 받는다
    field = [list(map(int, input().split())) for _ in range(N)]
    # 사각형의 넓이를 넣을 리스트를 만든다
    area = []
    # 게임판의 왼쪽 상단 좌표를 순회하면서
    for i1 in range(N):
        for j1 in range(N):
            # 이에 따른 알맞은 범위의 우측 하단 좌표를 순회하면서
            for i2 in range(i1, N):
                for j2 in range(j1, N):
                    # 자기 자신과 같은 좌표일 경우 제외
                    if i1 != i2 or j1 != j2:                        
                        # 조건에 맞는 직사각형이 나올 경우
                        if field[i1][j1] == field[i2][j2]:
                            # 그 넓이를 리스트에 넣는다
                            area.append((i2-i1+1)*(j2-j1+1))
    # 직사각형이 하나도 나오지 않았다면
    if area == []:
        # 테케와 0을 출력
        print(f'#{tc} 0')
    # 그렇지 않다면
    else:
        # 테케와 최댓값의 넓이를 가진 직사각형의 개수를 출력
        print(f'#{tc} {area.count(max(area))}')