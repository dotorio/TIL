import sys
sys.stdin = open('input1.txt')

T = int(input())
for i in range(1, T+1):
    N = int(input())
    num = list(map(int, input()))
    one_list = []
    for j in range(N):
        if num[j] == 1:
            one_length = 1
            for x in range(1, N):
                if j+x > N-1 or num[j+x] != 1:
                    one_list.append(one_length)
                    break
                else:
                    one_length += 1
    print(f'#{i} {max(one_list)}')