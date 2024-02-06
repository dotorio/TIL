N = int(input())
arr = []
for _ in range(N):
    a, b = map(int, input().split())
    arr.append([b, a])
arr.sort()
for i in arr:
    i[0], i[1] = i[1], i[0]
    print(*i)