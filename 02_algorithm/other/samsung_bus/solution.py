import sys
sys.stdin = open('input.txt')

T = int(input())
for case in range(1, T+1):
    N = int(input())
    bus = [list(map(int, input().split())) for i in range(N)]
    P = int(input())
    bus_sta = []
    bus_cnt = []
    for k in range(P):
        bus_sta.append(int(input()))
        bus_cnt.append(0)
    for i in range(N):
        for j in range(P):
            if bus[i][0] <= bus_sta[j] <= bus[i][1]:
                bus_cnt[j] += 1
    retult = " ".join(map(str, bus_cnt))
    print(f'#{case} {retult}')


