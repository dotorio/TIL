import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    formula = input()
    stack = []
    i = 0
    while i < N:
        if formula[i].isdigit():
            stack.append(int(formula[i]))
            i += 1
        elif formula[i] == '*':
            stack.append(stack.pop() * int(formula[i+1]))
            i += 2
        else:
            i += 1
    print(f'#{tc} {sum(stack)}')
        
