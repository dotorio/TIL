import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    metals = input()
    while '()' in metals:
        new_metals = metals.replace('()','L')
        metals = new_metals
    cut = 0
    stack = 0
    for i in metals:
        if i == '(':
            cut += 1
            stack += 1
        if i == 'L':
            cut += stack
        if i == ')':
            stack -= 1
                    
    print(f'#{tc} {cut}')

