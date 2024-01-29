N = 6
arr = [7, 2, 5, 3, 1, 4]

def asc(arr, N): # 오름차순
    for i in range(N-1, 0, -1): # 정렬할 구간의 마지막 인덱스
        for j in range(i): # 비교할 두 원소 중 왼쪽의 인덱스
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                
def dec(arr, N): # 내림차순
    for i in range(N-1, 0, -1): # 정렬할 구간의 마지막 인덱스
        for j in range(i): # 비교할 두 원소 중 왼쪽의 인덱스
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]    

dec(arr, N)
print(arr)

