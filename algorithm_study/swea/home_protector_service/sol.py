import sys
sys.stdin = open('input.txt')

def check():
    global max_cnt
    # city를 순회할 것이다
    for i in range(N):
        for j in range(N):
            # 집들과의 거리를 기록할 리스트를 생성
            D = [0]*2*N
            # 집의 좌표를 순회하며 시티의 좌표와의 거리를 인덱스로 하는
            # 리스트의 값을 1 올림(해당 거리의 집 개수를 표시하는 용도)
            for y, x in home:
                D[abs(i-y)+abs(j-x)+1] += 1
            # 거리를 기록한 리스트를 거꾸로 순회
            for k in range(2*N-1, 0, -1):
                # 해당 거리에 집이 있다면
                if D[k]:
                    # 손해를 보지 않는다면
                    if sum(D)*M >= k**2+(k-1)**2:
                        # 서비스 제공받는 집의 개수를 갱신
                        max_cnt = max(max_cnt, sum(D))
                        # 만약 모든 집에 서비스를 제공할 수 있으면
                        if max_cnt == len_home:
                            # 즉시 종료
                            return
                        # 해당 좌표에서의 최댓값을 이미 알았으니 순회 종료
                        break
                    # 손해를 본다면
                    else:
                        # 해당 거리의 집 개수를 0으로 변경하고 다음 순회로
                        D[k] = 0

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    city = [list(map(int, input().split())) for _ in range(N)]
    # 집이 있는 좌표들을 리스트 안에 넣는다
    home = []
    for i in range(N):
        for j in range(N):
            if city[i][j]:
                home.append([i,j])
    # 집들의 개수를 상수로 받아둠
    len_home = len(home)
    # 마지막에 출력할 서비스를 제공받는 집들의 개수를 0으로 설정
    max_cnt = 0
    # 함수 호출 후 결과를 출력
    check()
    print(f'#{tc} {max_cnt}')


