import sys
sys.stdin = open('sample_input.txt')

def arr_sort(arr):
    for i in range(len(arr) - 1):
        the_min = i
        for j in range(i+1, len(arr)):
            if arr[the_min] > arr[j]:
                the_min = j
        arr[i], arr[the_min] = arr[the_min], arr[i]

T = int(input())
for case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    # arr.sort()

    arr_sort(arr)

    special = []
    for i in range(5):
        special.append(arr[-(i+1)])
        special.append(arr[i])
    
    print(f'#{case}', end = " ")
    print(*special)
