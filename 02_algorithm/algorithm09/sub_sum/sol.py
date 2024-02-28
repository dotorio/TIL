import sys
sys.stdin = open('input.txt')

def sub_sum(a, b, c):
    global cnt
    if c > K:
        return
    if c == K:
        cnt += 1
        return
    if a == b:
        return
    else:
        sub_sum(a+1, b, c+arr[a])
        sub_sum(a+1, b, c)

for tc in range(1, int(input())+1):
    N , K = map(int, input().split())
    arr = list(map(int, input().split()))
    cnt = 0
    sub_sum(0, N, 0)
    print(f'#{tc} {cnt}')