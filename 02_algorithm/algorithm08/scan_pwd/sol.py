import sys
sys.stdin = open('input.txt')

dec = ['0001101', '0011001', '0010011', '0111101', '0100011',
       '0110001', '0101111', '0111011', '0110111', '0001011']

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    visited = [[0]*M for _ in range(N)]
    ans_sum = 0
    i = 0
    while i <= N-1:
        for j in range(M-1, -1, -1):
            if arr[i][j] == '1' and visited[i][j] == '0':
                recent = arr[i][j]
                last_x, last_y, length, cnt = i, j, 1, 1
                j -= 1
                while cnt != 4:
                    if arr[i][j] == recent:
                        pass
                    else:
                        arr[i][j] = recent
                        cnt += 1
                    j -= 1    
                    length += 1
                ratio = length // 8 + 1
                가 = last_y-ratio*64+1
                enc = arr[i][가:last_y + 1]
                while arr[last_x][last_y] == '1':
                    for k in range(가, last_y+1):
                        visited[last_x][k] = 1
                    last_x -= 1
                pwd, sum, = 0, 0
                for q in range(8):
                    암호 = enc[8*q*ratio:8*(q+1)*ratio]
                    번호 = ''
                    for w in range(8):
                        번호 = 번호 + 암호[8*w]
                    if 번호 in dec:
                        if q % 2 == 0:
                            pwd += dec.index(번호) * 3
                        else:
                            pwd += dec.index(번호)
                        sum += dec.index(번호)
                    else:
                        continue
                if pwd % 10 == 0:
                    ans_sum += sum
        i += 1
    print(f'#{tc} {ans_sum}')
                
                























