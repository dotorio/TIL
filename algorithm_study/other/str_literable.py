N = int(input())
for i in range(N):
    A, B = map(str, input().split())
    C = int(A)
    for j in B:
        print(j * C, end = "")
    if i != N-1:
        print()
