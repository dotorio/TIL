import sys
sys.stdin = open('input.txt')

# 10개의 테스트케이스
for tc in range(1, 11):
    # 정사각형 테이블의 한 변의 길이
    N = int(input())
    # 정사각형 테이블
    table = [list(map(int, input().split())) for _ in range(N)]
    # 출력할 교착 상태의 개수
    cnt = 0
    # 열, 행 이중 순회할 것이다
    for j in range(N):
        # N극을 만나면 True로 변경할 것이다
        magnet = False
        for i in range(N):
            # N극을 만나면 True
            if table[i][j] == 1:
                magnet = True
            # S극을 만났을 때 이전에 N극이 있었다면 교착 상태 발생
            elif table[i][j] == 2 and magnet:
                # 교착 상태를 1 올리고
                cnt += 1
                # 교착 상태를 지났으므로 False로 변경
                magnet = False
    # 테케와 교착 상태의 개수를 출력
    print(f'#{tc} {cnt}')