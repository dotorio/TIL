N = int(input())

# 공백으로 이루어진 배열을 생성
arr = [[' ']*(2*N-1) for _ in range(N)]

def f(arr, A, B, C, D):

    # 세로 차이가 3 난다면
    # 규칙에 맞게 별을 채워서 리턴
    if B-A == 3:
        for i in range(A, B):
            if i == A:
                arr[i][C+2] = '*'
            elif i == A+1:
                arr[i][C+1] = arr[i][C+3] = '*'
            else:
                arr[i][C:D-1] = ['*']*5
        return arr
    
    # 세로 차이가 3보다 더 난다면 분할 정복
    else:
        f(arr, A, A+(B-A)//2, C+(D-C)//4, C+(D-C)//4*3)
        f(arr, A+(B-A)//2, B, C, C+(D-C)//2)
        f(arr, A+(B-A)//2, B, C+(D-C)//2, D)
        return arr

# 처음 함수 호출                        
f(arr, 0, N, 0, 2*N)

# 완성된 배열을 출력
for i in arr:
    print("".join(i))