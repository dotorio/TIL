import sys
sys.stdin = open('input.txt')

dec = ['0001101', '0011001', '0010011', '0111101', '0100011',
       '0110001', '0101111', '0111011', '0110111', '0001011']

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    visited = [[0]*M for _ in range(N)]
    answer_sum = 0
    for i in range(N):
        for j in range(M-1, -1, -1):
            if arr[i][j] != '0' and visited[i][j] == 0:
                password_0b = bin(int(arr[i][j], 16))[2:].zfill(4)
                last_x, last_y = i, j
                find_ratio = False
                find_zero_cnt = False
                ratio = 0
                while not find_ratio:
                    ratio += 1
                    password_0b = '0' * (8-len(bin(int(arr[last_x][last_y-2:last_y], 16))[2:].zfill(4))) + bin(int(arr[last_x][last_y-2:last_y], 16))[2:].zfill(4) + password_0b
                    if not find_zero_cnt:
                        find_zero_cnt = True
                        zero_cnt = 0
                        while password_0b[-(zero_cnt+1)] == '0':
                            zero_cnt += 1
                    end = -(zero_cnt+1)
                    change_num_cnt = 0
                    for k in range(7*ratio):
                        if password_0b[end-k] != password_0b[end-k-1]:
                            change_num_cnt +=1
                    if change_num_cnt >= 4:
                        find_ratio = True
                        if end == -1:
                            real_pwd = bin(int(arr[i][j-14*ratio:j+1], 16))[2:].zfill(4)
                        else:
                            real_pwd = bin(int(arr[i][j-14*ratio:j+1], 16))[2:].zfill(4)[:end+1]
                        real_pwd = '0' * ((56*ratio)-len(real_pwd)) + real_pwd
                        if len(real_pwd) == 56*ratio + 4:
                            real_pwd = real_pwd[4:]
                    else:
                        last_y -= 2
                while arr[last_x][j] != '0':
                    change_arr = [1] * (14 * ratio + 1)
                    visited[last_x][j-14*ratio:j+1] = change_arr
                    last_x += 1
                pwd, sum = 0, 0
                for k in range(8):
                    if k % 2 == 0:
                        pwd += dec.index(real_pwd[7*k*ratio : 7*(k+1)*ratio : ratio]) * 3
                    else:
                        pwd += dec.index(real_pwd[7*k*ratio : 7*(k+1)*ratio : ratio])
                    sum += dec.index(real_pwd[7*k*ratio : 7*(k+1)*ratio : ratio])
                if pwd % 10 == 0:
                    answer_sum += sum
    print(f'#{tc} {answer_sum}')
