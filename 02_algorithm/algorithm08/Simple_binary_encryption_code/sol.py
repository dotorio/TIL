import sys
sys.stdin = open('input.txt')

dec = ['0001101', '0011001', '0010011', '0111101', '0100011',
       '0110001', '0101111', '0111011', '0110111', '0001011']

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    find = False
    for i in arr:
        for j in range(M-1, -1, -1):
            if i[j] == '1':
                enc = i[j-55:j+1]
                find = True
                break
        if find == True:
            break
    pwd, sum = 0, 0
    for i in range(8):
        for j in range(10):
            if enc[7*i:7*(i+1)] == dec[j]:
                if i % 2 == 1:
                    pwd += j
                else:
                    pwd += j*3
                sum += j
                break
    if pwd % 10 == 0:
        print(f'#{tc} {sum}')
    else:
        print(f'#{tc} 0')