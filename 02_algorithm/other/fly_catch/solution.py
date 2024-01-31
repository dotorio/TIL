import sys
sys.stdin = open('input.txt')

T = int(input())
for case in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for i in range(N)]
    max_fly_catch = 0
    for y in range(N-M+1):
        for x in range(N-M+1):
            catch_list = []
            for i in range(M):
                catch_list.append(arr[x + i][y : y + M])
            fly_catch = 0
            for j in catch_list:
                fly_catch += sum(j)
            if max_fly_catch < fly_catch:
                max_fly_catch = fly_catch
    print(f'#{case} {max_fly_catch}')