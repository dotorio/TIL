import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    metals = input()
    while '()' in metals:
        new_metals = metals.replace('()','L')
        metals = new_metals
    cut = 0
    while '(' in metals:
        for i in range(len(metals)):
            if metals[i] == '(':
                cut += 1
                j = i
                stack = 0
                while stack >= 0 or metals[j] != ')':
                    j += 1
                    if j > len(metals) -1:
                        break
                    if stack <=0 and metals[j] == ')':
                        break
                    if metals[j] == '(':
                        stack += 1
                    elif metals[j] == 'L':
                        cut += 1
                    else:
                        stack -= 1
                new_metals = metals.replace('(','M',1)
                metals = new_metals

                    
    print(f'#{tc} {cut}')

