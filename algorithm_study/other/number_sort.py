N = int(input())
list = []
for _ in range(N):
    a = int(input())
    if a not in list:
        list.append(a)
list.sort()
for i in list:
    print(i)