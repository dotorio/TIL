import sys
sys.stdin = open('input.txt')

T = int(input())
for case in range(1, T+1):
    print(f'#{case}')
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr2 = list(map(list, zip(*arr[::-1])))
    arr3 = list(map(list, zip(*arr2[::-1])))
    arr4 = list(map(list, zip(*arr3[::-1])))
    for i in range(N):

        print("".join(map(str, arr2[i])), end = " ")
        print("".join(map(str, arr3[i])), end = " ")
        print("".join(map(str, arr4[i])))

