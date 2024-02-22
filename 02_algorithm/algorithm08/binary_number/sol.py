import sys
sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

for tc in range(1, int(input())+1):
    N, num = input().split()
    # 마지막에 출력할 결과를 만들어놓는다
    result = ''
    # 숫자의 자릿수만큼 반복
    for i in range(int(N)):
        # 각 자릿수를 10진수로 바꿈
        num_digit = int('0x' + num[i], 16)
        # 2진수로 바꿀 결과를 만들어놓는다
        bin = ''
        # 4자리 2진수는 8로 나누면 정수 몫이 1 or 0이다
        std = 8
        # 4번 반복하며 1 or 0을 bin에 넣는다
        for _ in range(4):
            if num_digit // std == 1:
                bin = bin + '1' 
                num_digit -= std
            else:
                bin = bin + '0'
            std //= 2
        # 2진수로 바꾼 결과를 result에 넣는다
        result = result + bin
    print(f'#{tc} {result}')