import sys
sys.stdin = open('input.txt')

for tc in range(int(input())):
    N = int(input())
    carrot = list(map(int, input().split()))
    ctn = []
    cnt = 1
    for i in range(N):
        if i == N-1:
            ctn.append(cnt)
        elif carrot[i] < carrot[i+1]:
            cnt += 1
        else:
            ctn.append(cnt)
            cnt = 1
    print(f'#{tc+1} {max(ctn)}')
