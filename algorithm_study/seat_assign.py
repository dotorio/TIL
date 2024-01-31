C, R = map(int, input().split())
# 공연장의 격자 크기를 받는다.
K = int(input())
# 대기번호를 받는다.
start_x = 1
start_y = 0
# 쳣 좌표를 설정한다.

def move(Col, Row, Wait, x, y):

    for i in range(Row):
        if Wait == 0:
            break
        y += 1
        Wait -= 1
        # 열의 수만큼 위로 올라가면서 대기번호를 1 뺀다
        # 대기번호가 0이라면 멈춘다.
        
    for i in range(Col-1):
        if Wait == 0:
            break
        x += 1
        Wait -= 1
        # (행-1)의 수만큼 오른쪽으로 가면서 대기번호를 1 뺀다
        # 대기번호가 0이라면 멈춘다.
        
    for i in range(Row-1):
        if Wait == 0:
            break
        y -= 1
        Wait -= 1
        # (열-1)의 수만큼 아래로 내려가면서 대기번호를 1 뺀다
        # 대기번호가 0이라면 멈춘다.

    for i in range(Col-2):
        if Wait == 0:
            break
        x -= 1
        Wait -= 1
        # (행-2)의 수만큼 왼쪽으로 가면서 대기번호를 1 뺀다
        # 대기번호가 0이라면 멈춘다.

    if Wait != 0:
        return move(Col-2, Row-2, Wait, x, y)
    else:
        return [x, y]
    # 한바퀴를 돌고 대기번호가 남아있다면
    # 행 수, 열 수에 2를 빼고 재귀함수 호출
    # 대기번호가 0이라면 현재 좌표를 리턴
        

if K > C * R:
    print(0)
# 만약 좌석을 배정할 수 없으면 0을 출력
else:
    print(*(move(C, R, K, start_x, start_y)))
# 좌석을 배정할 수 있으면 재귀함수를 통해 좌표를 출력