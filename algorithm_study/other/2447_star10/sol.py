# N = int(input())
# arr = [['*'] * N for _ in range(N)]

# def f(arr):
#     len_arr = len(arr)
#     if len_arr == 1:
#         return
#     else:
#         for i in range(3):
#             for j in range(3):
#                 if i == 1 and j == 1:
#                     for x in range(len_arr//3, len_arr//3*2):
#                         for y in range(len_arr//3, len_arr//3*2):
#                             arr[x][y] = ' '
#                 else:
#                     new_arr = []
#                     for x in range(len_arr//3*i, len_arr//3*(i+1)):
#                         new_arr.append(arr)
# f(arr)
# for i in arr:
#     print("".join(i))
a = [[1,2,3],[3,4,5]]
b = a[0][1:]
b[0]= 10
print(b)
print(a)
