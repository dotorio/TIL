import sys
sys.stdin = open('input.txt')

T = int(input())
for case in range(1, T+1):
    num = int(input())
    arr = [0] * 5
    arr_2 = [2, 3, 5, 7, 11]
    for a in arr_2:
        while num % a == 0:
            arr[arr_2.index(a)] += 1
            num /= a 

    print(f'#{case} {" ".join(map(str, arr))}')
