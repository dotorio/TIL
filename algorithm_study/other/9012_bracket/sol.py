import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    bra = input()
    stack = 0
    result = 'YES'
    for i in bra:
        if stack < 0:
            reslut = 'NO'
            break
        elif i == '(':
            stack += 1
        elif i == ')':
            stack -= 1
    if stack != 0:
        result = 'NO'
    print(result)