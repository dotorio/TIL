import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    infix = input()
    # 숫자를 저장할 스택
    stack = []
    # 수식의 위치를 가져올 i를 0으로 지정
    i = 0
    # i가 수식의 길이를 넘을 때까지 반복
    while i < N:
        # 해당 위치가 숫자라면 스택에 저장하고 i를 1 올림
        if infix[i].isdigit():
            stack.append(int(infix[i]))
            i += 1
        # 해당 위치가 * 라면 이전 숫자와 다음 숫자를 곱해서 스택에 저장
        # i를 2 올림
        elif infix[i] == '*':
            stack.append(stack.pop() * int(infix[i+1]))
            i += 2
        # 해당 위치가 + 라면 i를 1 올리고 패스
        else:
            i += 1
    # 테케와 스택에 저장된 수의 합을 출력
    print(f'#{tc} {sum(stack)}')