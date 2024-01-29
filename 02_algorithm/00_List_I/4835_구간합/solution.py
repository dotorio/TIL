import sys
sys.stdin = open('sample_input.txt')\

T = int(input())
for case in range(T):
    N, M = map(int, input().split())
    number_list = list(map(int, input().split()))
    new_list = []
    for number in range(N-M+1):
        number_sum = 0
        for new_num in range(M):
            number_sum += number_list[number+new_num]
        new_list.append(number_sum)
    print(f'#{case+1} {max(new_list)-min(new_list)}')
