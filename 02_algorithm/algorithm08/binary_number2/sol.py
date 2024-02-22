import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input())+1):
    N = float(input())
    # 출력할 ans를 빈 문자열로 할당
    ans = ''
    # 계산한 횟수를 cnt로 할당
    cnt = 0
    # 처음 기준인 0.5를 std로 할당
    std = 0.5
    # 계산한 횟수가 12 이하이면 True, 아니면 False
    result = True
    # N이 0이 될때까지 반복
    while N != 0:
        # 계산을 12번 했었다면 overflow 출력하고 break
        if cnt == 12:
            result = False
            print(f'#{tc} overflow')
            break
        # N이 기준보다 크다면 ans에 1 넣고 N에 기준 빼기
        if N >= std:
            ans = ans + '1'
            N -= std
        # N이 기준보다 작다면 ans에 0 넣기
        else:
            ans = ans + '0'
        # 기준을 2로 나누고 계산 횟수를 1 올린다
        std /= 2
        cnt += 1
    # result가 True라면 결과를 출력
    if result == True:
        print(f'#{tc} {ans}')