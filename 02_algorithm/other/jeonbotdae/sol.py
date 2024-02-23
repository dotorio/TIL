import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input())+1):
    jbd = []
    cnt = 0
    for i in range(int(input())):
        A, B = map(int, input().split())
        for j in jbd:
            if j[0] > A and j[1] < B:
                cnt += 1
            elif j[0] < A and j[1] > B:
                cnt += 1
        jbd.append([A, B])
    print(f'#{tc} {cnt}')