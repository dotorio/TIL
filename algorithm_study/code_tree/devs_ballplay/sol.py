import sys
sys.stdin = open('input.txt')

# n = int(input())
# a = list(map(int, input().split()))
# a.sort()
# print(a)

N = int(input())
devs = list(map(int, input().split()))
devs.sort()
print(devs)
ball = 0
while devs:
    start = devs.pop()
    if not devs:
        print(f'스타트는 {start}')
        ball += 1
        break
    next = devs.pop()
    min_dis = start - next
    while devs:
        if min_dis < next - devs[-1]:
            break
        min_dis = next - devs[-1]
        next = devs.pop()
    print(f'dis는 {min_dis}')
    print(next)
    ball += 1
print(ball)