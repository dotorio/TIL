import sys
sys.stdin = open('input.txt')

def f(cnt, stack):
    num = stack.pop()
    if num == N:
        return cnt
    if len(stack) == 1:
        if (N > 10 and num // 2 >= N) or num//10 >= N+1:
            if num%2:
                return f(cnt+1, [num-1, num+1])
            else:
                return f(cnt+1, [num//2])
    
    f(cnt+1, num-1)


for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    print(f'#{tc} {f(0, [M])}')