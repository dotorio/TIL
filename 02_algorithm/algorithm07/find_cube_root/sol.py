import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input())+1):
    N = int(input())
    i = 1
    result = False
    while i**3 <= N:
        if i**3 == N:
            result = True
            print(f'#{tc} {i}')
            break
        i += 1
    if result == False:
        print(f'#{tc} -1')