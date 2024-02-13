import sys
sys.stdin = open('sample_input.txt')

ope = ['+', '*', '.']

T = int(input())
for tc in range(1, T+1):
    stack = []
    formula = list(input().split())
    for i in formula:
        if i not in ope:
            stack.append[i]
        elif len(stack) < 2:
            print(f'#{tc} error')
            break
        else:

