import sys
sys.stdin = open('input.txt')

T = int(input())
for case in range(1, T+1):
    print(f'#{case}')
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        new_arr_list = []
        for k in range(N):

        new_arr = []

        for j in range(N):
            if j != N-1:
                print("".join(new_arr[j]), end = " ")
            else:
                print("".join(new_arr[j]))

# arr = [[1, 2, 3],
#        [4, 5, 6],
#        [7, 8, 9]]
# new_arr = list(map(list, zip(*arr[::-1])))
# for i in new_arr:
#     print(i)

# print()

# new_arr2 = list(map(list, zip(*new_arr[::-1])))
# for i in new_arr2:
#     print(i)