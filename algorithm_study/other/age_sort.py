N = int(input())
a = {}
for _ in range(N):
    age, name = map(str, input().split())
    a[int(age)] = name
print(a)