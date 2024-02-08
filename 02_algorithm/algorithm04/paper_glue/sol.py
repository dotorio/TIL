import sys
sys.stdin = open('sample_input.txt')

def glue(num):
    if num == 10:
        return 1
    if num == 20:
        return 3
    return glue(num-10)+glue(num-20)*2

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    print(f'#{tc} {glue(N)}')