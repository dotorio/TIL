import sys
sys.stdin = open('input.txt')

for i in range(1, int(input())+1):
    num = str(i)
    if '3' in num or '6' in num or '9' in num:
        cnt = 0
        while '3' in num:
            cnt += 1
            num = num.replace("3", "", 1)
        while '6' in num:
            cnt += 1
            num = num.replace("6", "", 1)
        while '9' in num:
            cnt += 1
            num = num.replace("9", "", 1)
        print('-'*cnt, end = ' ')
    else:
        print(num, end= ' ')


