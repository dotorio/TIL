import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input())+1):
    N = int(input())
    # 출발시간, 도착시간을 기록할 time 리스트
    time = []
    # 확정된 사용시간을 기록할 cfm 리스트
    cfm = []
    # 사용할 화물차의 개수를 기록할 cnt
    cnt = 0
    # [도착시간, 출발시간] 모양으로 time에 넣는다
    for _ in range(N):
        S, E = map(int, input().split())
        time.append([E, S])
    # 도착시간 순으로 정렬
    time.sort()
    # time 리스트를 순회하며
    for i in time:
        # 출발시간부터 도착시간까지
        for j in range(i[1], i[0]):
            # 해당 시간이 확정된 사용시간이라면 break
            if j in cfm:
                break
            # 끝까지 break되지 않았다면 
            if j == i[0]-1:
                # cfm에 넣고 화물차 개수를 1 올린다
                cfm.extend(list(range(i[1], i[0])))
                cnt += 1
    # 테케와 화물차 개수를 출력
    print(f'#{tc} {cnt}')