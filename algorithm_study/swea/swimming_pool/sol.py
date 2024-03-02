import sys
sys.stdin = open('input.txt')

def check3(a, b):
    if a == 12:
        sum_list.append(b)
        return
    if sum(money[a:a+3]) > mon3:
        check3(min(12, a+3), b+mon3)
    check3(a+1, b+money[a])


for tc in range(1, int(input())+1):
    day, mon, mon3, year = map(int, input().split())
    per = list(map(int, input().split()))
    money = [0]*12
    for i in range(12):
        money[i] = min(mon, day*per[i])
    sum_list = []
    check3(0, 0)
    print(f'#{tc} {min(year, min(sum_list))}')
