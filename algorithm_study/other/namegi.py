a = set()
for i in range(10):
    A = int(input())
    a.add(A % 42)
print(len(a))