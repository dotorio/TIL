import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    print(f'#{tc}')
    arr = [1]
    for i in range(1, N+1):
        arr2 = [1] * i
        for j in range(1, i-1):
            arr2[j] = arr[j-1] + arr[j]
        print(" ".join(map(str, arr2)))
        arr = arr2