import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    money = [
    [50000, 0],
    [10000, 0],
    [5000, 0],
    [1000, 0],
    [500, 0],
    [100, 0],
    [50, 0],
    [10, 0]]
    N = int(input())
    for i in money:
        if i[0] > N:
            continue
        else:
            i[1] += N // i[0]
            N = N % i[0]
            if N == 0:
                break
    print(f'#{tc}')
    for i in money:
        print(i[1], end=" ")
    print()