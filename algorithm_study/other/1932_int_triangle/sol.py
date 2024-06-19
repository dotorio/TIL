import sys
sys.stdin = open('input.txt')

n = int(input())
arr = [-1]*n
for i in range(n):
    tri = list(map(int, input().split()))
    new_arr = []
    for j in range(i+1):
        if arr[j] == -1:
            if j == 0:
                new_arr.append(tri[0])
            else:
                new_arr.append(arr[j-1] + tri[j])
        elif j == 0:
            new_arr.append(arr[0] + tri[0])
        else:
            new_arr.append(max(arr[j-1], arr[j]) + tri[j])
    arr[:i+1] = new_arr
print(max(arr))