import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for case in range(T):
    N = int(input())
    number_list = list(map(int, input().split()))
    number_list.sort()
    print(f'#{case+1} {number_list[-1]-number_list[0]}')