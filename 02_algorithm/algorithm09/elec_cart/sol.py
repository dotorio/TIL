import sys
sys.stdin = open('input.txt')

def min_sum(a, b, c):
    if c >= min(sum_list):
        return
    if a == b:
        sum_list.append(c)
    else:
        for i in range(b):
            if a == i or arr2[i] == True:
                continue
            else:
                arr2[i] = True
                min_sum(a+1, b, c+arr[a][i])
                arr2[i] = False


for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    sum_list = [10000]
    arr2 = [False] * (N)
    min_sum(0, N, 0)
    print(f'#{tc} {min(sum_list)}')