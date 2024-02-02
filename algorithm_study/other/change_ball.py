N, M = map(int, input().split())
baguni = list(range(1, N+1))
for i in range(M):
    A, B = map(int, input().split())
    baguni[A-1], baguni[B-1] = baguni[B-1], baguni[A-1]
print(" ".join(map(str, baguni)))