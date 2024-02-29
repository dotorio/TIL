import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input())+1):
    room = [0]*200
    for std in range(int(input())):
        A, B = map(int, input().split())
        for i in range((min(A, B)-1)//2, (max(A, B)-1)//2+1):
            room[i] += 1
    print(f'#{tc} {max(room)}')