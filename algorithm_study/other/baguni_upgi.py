N, M = map(int, input().split())
baguni = list(range(1, N+1))
for i in range(M):
    A, B = map(int, input().split())
    arr = []
    for j in range(A-1, B):
        arr.append(baguni.pop(A-1))
    arr.reverse()
    for j in range(A-1, B):
        baguni.insert(j, arr.pop(0))
print(" ".join(map(str, baguni)))