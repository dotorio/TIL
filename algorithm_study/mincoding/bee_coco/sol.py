import sys
sys.stdin = open('input.txt')

# 8방향 표시
dy = [-1, -1, -1, 0, 0, 1, 1, 1]
dx = [-1, 1, 0, -1, 1, 0, -1, 1]

def find(loc, cnt, bnf):
    global max_bnf

    # 좌표 4개를 잡았다면 최대 이익 갱신
    if cnt == 4:
        max_bnf = max(max_bnf, bnf)
        return
    
    # 저장된 좌표마다
    for (y, x) in loc:

        # x가 홀수냐 짝수냐에 따라
        if not x%2:

            # 8방향에서 맞는 방향으로만 간다
            for i in range(6):
                new_y, new_x = y+dy[i], x+dx[i]

                # 이미 더한 좌표가 아니고 갈수 있는 좌표라면
                if (new_y, new_x) not in loc and 0<=new_y<N and 0<=new_x<M:
                    
                    # 좌표 리스트에 더하고 함수 호출
                    loc.append((new_y, new_x))
                    find(loc, cnt+1, bnf+bee[new_y][new_x])
                    
                    # 백트래킹
                    loc.pop()
        else:
            for i in range(2, 8):
                new_y, new_x = y+dy[i], x+dx[i]
                if (new_y, new_x) not in loc and 0<=new_y<N and 0<=new_x<M:
                    loc.append((new_y, new_x))
                    find(loc, cnt+1, bnf+bee[new_y][new_x])
                    loc.pop()

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    bee = [list(map(int, input().split())) for _ in range(N)]
    
    # 최대 이익을 0으로 설정한다
    max_bnf = 0

    # 각 좌표마다 함수 호출
    for y in range(N):
        for x in range(M):

            # 첫번째 인자는 이익에 더할 좌표 리스트
            # 두번째 인자는 리스트의 좌표 개수
            # 세번째 인자는 현재 누적 이익합
            find([(y, x)], 1, bee[y][x])

    # 완성된 최대 이익을 출력한다
    print(f'#{tc} {max_bnf}')