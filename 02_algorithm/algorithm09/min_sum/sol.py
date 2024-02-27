import sys
sys.stdin = open('input.txt')

def min_sum(a, b, c, d):
    if d >= min(sum_list):
        return
    if a == c or b == c:
        sum_list.append(d)
        return
    else:
        if a == c-1:
            min_sum(a, b+1, c, d+arr[a][b])
        elif b == c-1:
            min_sum(a+1, b, c, d+arr[a][b])
        else:
            min_sum(a+1, b, c, d+arr[a][b])
            min_sum(a, b+1, c, d+arr[a][b])

for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    sum_list = [999999]
    min_sum(0, 0, N, 0)
    print(f'#{tc} {min(sum_list)}')