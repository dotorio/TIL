import sys
sys.stdin = open('input.txt')
from collections import deque

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    cheese = deque(map(int, input().split()))
    # 피자 번호를 데크 형태로 만든다
    pizza_num = deque(range(1, M+1))
    # 화덕을 데크 형태로 만들어서
    # 화덕의 크기만큼 피자 번호, 치즈를 꺼내서
    # [피자 번호, 치즈] 형태로 화덕에 넣는다
    hwadeok = deque()
    for i in range(N):
        hwadeok.append([pizza_num.popleft(), cheese.popleft()])
    # 화덕에 피자가 하나 남을 때까지 반복한다
    while len(hwadeok) != 1:
        # 화덕 맨 앞의 피자 치즈를 녹인다
        hwadeok[0][1] //= 2
        # 치즈가 0이 되면 화덕에서 빼낸다
        if hwadeok[0][1] == 0:
            hwadeok.popleft()
            # 화덕에 넣지 않은 피자가 남아있다면 넣는다
            if pizza_num:
                hwadeok.append([pizza_num.popleft(), cheese.popleft()])
        # 치즈가 0이 되지 않았다면 화덕 마지막에 넣는다
        else:
            hwadeok.append(hwadeok.popleft())
    # 마지막에 남은 피자의 번호를 출력한다
    print(f'#{tc} {hwadeok[0][0]}')