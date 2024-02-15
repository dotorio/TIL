# N = int(input())
# arr = [['*'] * N for _ in range(N)]
#
# def f(arr, A, B, C, D):
#     if B-A == 1:
#         return arr
#     else:
#         for i in range(3):
#             for j in range(3):
#                 if i == 1 and j == 1:
#                     for x in range(A+(B-A)//3, A+(B-A)//3*2):
#                         for y in range(C+(D-C)//3, C+(D-C)//3*2):
#                             arr[x][y] = ' '
#                     return arr
#                 else:
#                     return f(arr, A+(B-A)//3*i, A+(B-A)//3*(i+1), C+(D-C)//3*j, C+(D-C)//3*(j+1))
# f(arr, 0, N, 0, N)
# for i in arr:
#     print("".join(i))

N = int(input())
arr = [['*'] * N for _ in range(N)]

def f(arr, A, B, C, D):
    if B-A == 1:
        return arr
    else:
        for i in range(3):
            for j in range(3):
                if i == 1 and j == 1:
                    for x in range(A+(B-A)//3, A+(B-A)//3*2):
                        for y in range(C+(D-C)//3, C+(D-C)//3*2):
                            arr[x][y] = ' '
                else:
                    f(arr, A+(B-A)//3*i, A+(B-A)//3*(i+1), C+(D-C)//3*j, C+(D-C)//3*(j+1))
        return arr

f(arr, 0, N, 0, N)
for i in arr:
    print("".join(i))