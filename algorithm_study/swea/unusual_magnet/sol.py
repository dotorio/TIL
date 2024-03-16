import sys
sys.stdin = open('input.txt')
from collections import deque

def f(num, rot):
    # 방문한 자석을 표시하고
    visit[num] = 1
    # 회전할 방향을 표시한다
    change[num] = rot
    # 왼쪽 자석도 회전해야 한다면
    if num-1 >= 0 and not visit[num-1] and magnet[num-1][2] != magnet[num][6]:
        # 기존 회전 방향과 반대로 해서 함수 호출
        if rot == 1:
            f(num-1, -1)
        else:
            f(num-1, 1)
    # 오른쪽 자석도 회전해야 한다면
    if num+1 < 4 and not visit[num+1] and magnet[num][2] != magnet[num+1][6]:
        # 기존 회전 방향과 반대로 해서 함수 호출
        if rot == 1:
            return f(num+1, -1)
        else:
            return f(num+1, 1)

for tc in range(1, int(input())+1):
    K = int(input())
    # 자석 정보를 데크로 받아 전체를 리스트로 묶는다
    magnet = [deque(map(int, input().split())) for _ in range(4)]
    for _ in range(K):
        # 회전하는 자석 번호와 회전 방향을 받음
        mag, rot = map(int, input().split())
        # 방문을 표시할 리스트, 회전 방향을 표시할 리스트를 만듬
        visit, change = [0]*4, [0]*4
        # 최초 자석 번호와 회전 방향으로 함수를 호출
        f(mag-1, rot)
        # 완성된 change 리스트를 순회
        for i in range(4):
            # 방향이 설정되어 있다면 그에 맞게 회전시켜준다
            if change[i]:
                if change[i] == 1:
                    magnet[i].appendleft(magnet[i].pop())
                else:
                    magnet[i].append(magnet[i].popleft())
    # 마지막 자석의 0번 인덱스부터 합쳐서 이진수를 만든다
    num = str(magnet[3][0]) + str(magnet[2][0]) + str(magnet[1][0]) + str(magnet[0][0])
    # 십진수로 변환해 출력한다
    print(f'#{tc} {int(num, 2)}')
