import sys
sys.stdin = open('input.txt')

def check(a):
    global result
    for i in range(10):
        if a[i] >= 3:
            result = True
            print(f'#{tc} {a[10]}')
        if not result and i <= 7 and a[i] > 0:
            if a[i+1] > 0 and a[i+2] > 0:
                result = True
                print(f'#{tc} {a[10]}')
        if result:
            break


for tc in range(1, int(input())+1):
    cards = list(map(int, input().split()))
    p1, p2 = [0]*10 + [1], [0]*10 + [2]
    result = False
    for i in range(12):
        if i % 2 == 0:
            p1[cards[i]] += 1
        else:
            p2[cards[i]] += 1
        if i > 3:
            if i % 2 == 0:
                check(p1)
            else:
                check(p2)
        if result:
            break
    if not result:
        print(f'#{tc} 0')

