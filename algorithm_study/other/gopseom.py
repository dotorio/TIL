A = int(input())
B = str(input())

arr = []

for i in B:
    arr.append(i)
print(A * int(arr[2]))
print(A * int(arr[1]))
print(A * int(arr[0]))
print(A * int(B))