C, R = map(int, input().split())
K = int(input())
# 변수를 받는다
start_x = 1
start_y = 0
# 쳣 좌표를 설정한다.

def move(Col, Row, Wait, x, y):

    for i in range(Row):
        if Wait == 0:
            break
        y += 1
        Wait -= 1
        
    for i in range(Col-1):
        if Wait == 0:
            break
        x += 1
        Wait -= 1
        
    for i in range(Row-1):
        if Wait == 0:
            break
        y -= 1
        Wait -= 1

    for i in range(Col-2):
        if Wait == 0:
            break
        x -= 1
        Wait -= 1
    if Wait != 0:
        return move(Col-2, Row-2, Wait, x, y)
    else:
        return [x, y]
        

if K > C * R:
    print(0)
# 만약 좌석을 배정할 수 없으면 0을 출력
else:
    print(*(move(C, R, K, start_x, start_y)))
# 좌석을 배정할 수 있으면 재귀함수를 통해 좌표를 출력


