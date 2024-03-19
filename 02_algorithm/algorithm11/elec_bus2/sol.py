import sys, time
sys.stdin = open('input.txt')

def go(start, start_b, change):
    # 마지막 정류장에 도달하면 자동 종료될 것이다
    while True:
        # will_go = 현재 배터리로 도달할 수 있는 정류장들의 리스트
        # with_b = 도달한 정류장에서 교체한 배터리로 갈 수 있는 정류장들의 리스트
        will_go, with_b = [], []
        # 배터리만큼 앞으로 간다
        for i in range(1, start_b+1):
            # 만약 마지막 정류장이라면
            if start+i == stop-1:
                # 즉시 교체 횟수를 반환
                return change
            # 마지막 정류장이 아니라면
            if start+i < stop-1:
                # 도달한 곳을 기록
                will_go.append(start + i)
                # 도달한 곳에서 배터리를 교체했을 때 갈 수 있는 정류장을 기록
                with_b.append(start + i + battery[start + i])
        # 다음 시작점은 with_b의 최댓값 인덱스에 대응되는 will_go
        start = will_go[with_b.index(max(with_b))]
        # 다음 배터리는 다음 시작점의 배터리
        start_b = battery[start]
        # 교체 횟수를 1 더해준다
        change += 1

# start_time = time.time()
for tc in range(1, int(input())+1):
    stop, *battery = map(int, input().split())
    # 시작 정류장을 0, 시작 배터리를 battery[0], 교체 횟수를 0으로 함수 호출     
    print(f'#{tc} {go(0, battery[0], 0)}')
# end_time = time.time()
# print("실행 시간: {:.6f} 초".format(end_time-start_time))