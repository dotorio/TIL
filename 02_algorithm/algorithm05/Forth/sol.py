import sys
sys.stdin = open('sample_input.txt')

# 테스트의 개수를 받는다
T = int(input())
# 각 테스트마다
for tc in range(1, T+1):
    # 스택을 만든다
    stack = []
    # 후위표기식을 리스트로 받는다
    formula = list(input().split())
    # 후위표기식을 순회하면서
    for i in formula:
        # 만약 연산자나 .이 아니라면
        if i not in ['+', '-', '*', '/', '.']:
            # 스택에 넣는다
            stack.append(i)
        # 만약 i가 .이라면
        elif i == '.':
            # 스택에 남은 것이 하나가 아니라면
            if len(stack) != 1:
                # 에러를 띄운다
                print(f'#{tc} error')
            # 스택에 남은 것이 하나라면
            else:
                # 양식에 맞게 출력한다
                print(f'#{tc} {stack.pop()}')
        # 만약 i가 연산자인데 스택에 2개 이상 남아있지 않다면
        elif len(stack) < 2:
            # 에러를 띄우고
            print(f'#{tc} error')
            # 즉각 멈춘다
            break
        # 이하는 스택에서 2개를 빼내서
        # 사칙연산에 맞게 계산해서 스택에 넣어주는 과정
        elif i == '+':
            now = int(stack.pop())
            stack.append(int(stack.pop()) + now)
        elif i == '-':
            now = int(stack.pop())
            stack.append(int(stack.pop()) - now)
        elif i == '*':
            now = int(stack.pop())
            stack.append(int(stack.pop()) * now)
        else:
            now = int(stack.pop())
            stack.append(int(stack.pop()) // now)
    

