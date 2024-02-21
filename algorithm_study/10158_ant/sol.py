# 격자의 크기와 개미의 좌표와 시간을 받는다
w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())
# 개미의 x좌표는 격자의 가로*2만큼 가면
# 원래대로 돌아오므로 시간을 가로*2로 나누고
# 남은 나머지만 남긴다
rightleft = t % (2 * w)
# 개미의 y좌표는 격자의 세로*2만큼 가면
# 원래대로 돌아오므로 시간을 세로*2로 나누고
# 남은 나머지만 남긴다
updown = t % (2 * h)
# 처음에는 오른쪽, 위쪽으로 가므로
# 방향을 설정해준다
right = True
up = True
# 가로로 움직일 시간이 남아 있을 때까지 반복
while rightleft:
    # 개미가 격자 오른쪽 끝에 있다면
    # 방향을 왼쪽으로 바꾼다
    if p == w:
        right = False
    # 개미가 격자 왼쪽 끝에 있다면
    # 방향을 다시 오른쪽으로 바꾼다
    elif p == 0:
        right = True
    # 방향에 맞게 움직이고 움직일 시간을 1 줄인다
    if right == True:
        p += 1
        rightleft -= 1
    else:
        p -= 1
        rightleft -= 1
# 세로로 움직일 시간이 남아 있을 때까지 반복
while updown:
    # 개미가 격자 위쪽 끝에 있다면
    # 방향을 아래쪽으로 바꾼다
    if q == h:
        up = False
    # 개미가 격자 아래쪽 끝에 있다면
    # 방향을 다시 위쪽으로 바꾼다
    elif q == 0:
        up = True
    # 방향에 맞게 움직이고 움직일 시간을 1 줄인다
    if up == True:
        q += 1
        updown -= 1
    else:
        q -= 1
        updown -= 1
print(p, q)