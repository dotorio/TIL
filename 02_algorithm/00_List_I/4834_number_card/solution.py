import sys
sys.stdin = open('sample_input.txt')


T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input()))
    num_list = [0]*10
    for i in A:
        num_list[i] += 1
    max_list = max(num_list)
    index_list = []
    for j, v in enumerate(num_list):
        if v == max_list:
            index_list.append(j)
    print(f'#{_+1} {max(index_list)} {max_list}')

    