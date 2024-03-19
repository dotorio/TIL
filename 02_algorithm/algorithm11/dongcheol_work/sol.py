import sys
sys.stdin = open('input.txt')

def f(idx, now_per):
    global max_per
    # 만약 현재 확률이 최대 확률보다 작다면
    if now_per <= max_per:
        # 즉시 손절
        return
    # 모든 사람에게 일을 주었다면
    if idx == N:
        # 최대 확률을 갱신하고 리턴
        max_per = max(now_per, max_per)
        return
    # 처리하지 않은 일을 주러 다음 사람에게 간다
    for j in range(N):
        if j not in visit:
            # 방문을 표시하고
            visit.append(j)
            # 함수 호출하고
            f(idx+1, now_per*per[idx][j]/100)
            # 다시 뺀다(백트래킹)
            visit.pop()

for tc in range(1, int(input())+1):
    N = int(input())
    per = [list(map(int, input().split())) for _ in range(N)]
    # 방문을 표시할 visit
    # 최대 확률은 0으로 설정해둔다
    visit, max_per = [], 0
    # idx는 0으로, 현재 확률은 1로 함수 호출
    f(0, 1)
    # 완성된 최대 확률을 소수점 6자리까지 출력한다
    print(f'#{tc} {"{:.6f}".format(max_per*100)}')