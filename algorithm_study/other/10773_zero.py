K = int(input())
arr = []
for i in range(K):
    A = int(input())
    if A == 0:
        arr.pop()
    else:
        arr.append(A)
print(sum(arr))