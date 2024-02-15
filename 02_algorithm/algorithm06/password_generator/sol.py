import sys
sys.stdin = open('input.txt')
from collections import deque

def generator(A):
    # 사이클을 돈다
    for i in range(1,6):
        now = A.popleft()-i
        # 빼고 나서 0 이하가 되었다면
        # 0으로 바꾸고 비밀번호 마지막에 넣는다
        if now <= 0:
            now = 0
            A.append(now)
            # 데크를 리스트로 바꿔서 출력한다        
            return f'#{tc} {" ".join(map(str, list(A)))}'
        # 빼고 난 값이 0보다 크다면
        # 비밀번호 마지막에 넣는다
        else:
            A.append(now)
    # 사이클을 돌아도 끝나지 않으면 한번 더 돈다
    return generator(A)

for _ in range(10):
    tc = int(input())
    password = deque(map(int, input().split()))
    # 숫자들이 적당히 크다면
    # 15의 배수를 적당히 빼서 함수 호출시 오류를 방지한다
    min_pwd = min(password)
    if min_pwd >= 25:
        for i in range(8):
            password[i] -= (min_pwd//15-1)*15
    # 함수의 결과를 출력한다
    print(generator(password))
   
