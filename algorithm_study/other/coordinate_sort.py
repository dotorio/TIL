N = int(input())
arr = []
for _ in range(N):
    a = list(map(int, input().split()))
    arr.append(a)
arr.sort()
for i in arr:
    print(" ".join(map(str, i)))