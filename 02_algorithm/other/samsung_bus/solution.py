import sys
sys.stdin = open('input.txt')

T = int(input())
for z in range(1, T+1):
    N = int(input())
    bus = []
    for j in range(N):
        A, B = map(int, input().split())
        bus.append([A, B])
    C = int(input())
    bus_sta = []
    bus_cnt = []
    for k in range(C):
        bus_sta.append(int(input()))
        bus_cnt.append(0)
    for j in range(N):
        for k in range(bus[j][0], bus[j][1]+1):
            for i in bus_sta:
                if k == i:
                    bus_cnt[bus_sta.index(i)] += 1
    retult = " ".join(map(str, bus_cnt))
    print(f'#{z} {retult}')


