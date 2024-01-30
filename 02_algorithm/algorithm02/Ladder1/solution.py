import sys
sys.stdin = open('input.txt')


def find_start(x, y):
    global left, right
    if y == 0:
        return x
    # y좌표가 0이라면 x좌표를 반환한다.
    if left == True:
        if x-1 >= 0 and arr[y][x-1] == 1:
            return find_start(x-1, y)
        # 이전 함수 결과의 방향이 왼쪽이라면,
        # 계속 왼쪽으로 가야 하는지 우선적으로 살펴본다.
        left = False
        return find_start(x, y-1)
    # 그렇지 않으면 위로 올라간다.
    if right == True:
        if x + 1 <= 99 and arr[y][x + 1] == 1:
            return find_start(x+1, y)
        # 이전 함수 결과에 방향이 오른쪽이라면,
        # 계속 오른쪽으로 가야 하는지 우선적으로 살펴본다.
        right = False
        return find_start(x, y-1)
    # 그렇지 않으면 위로 올라간다.
    if x - 1 >= 0 and arr[y][x - 1] == 1:
        left = True
        return find_start(x - 1, y)
    # 이전 함수 결과의 방향이 위쪽이라면,
    # 방향이 왼쪽으로 바뀌는지 살펴본다.
    if x + 1 <= 99 and arr[y][x + 1] == 1:
        right = True
        return find_start(x + 1, y)
    # 방향이 왼쪽으로 바뀌지 않는다면,
    # 방향이 오른쪽으로 바뀌는지 살펴본다.
    return find_start(x, y-1)
    # 둘다 아니면 위로 올라간다.
    
for a in range(1, 11):
    # 테스트의 개수는 총 10개
    case = int(input())
    # 테스트 번호
    arr = []
    # 배열을 담을 리스트를 만든다
    for b in range(100):
        arr.append(list(map(int, input().split())))
    # 100 * 100 배열을 input을 이용해 완성한다.
    for c in range(100):
        if arr[99][c] == 2:
            end = c
            break
    # 마지막 행의 2를 찾아 거꾸로 올라가서 시작 좌표를 찾을 것이다.
    left = False
    right = False
    # 첫 함수 결과는 위로 올라가야 하므로 방향을 둘다 False로 설정
    print(f'#{a} {find_start(c, 99)}')
    # 함수를 호출하여 첫 좌표를 얻어낸다.
    
