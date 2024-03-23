import sys
sys.stdin = open('input.txt')

n, q = map(int, input().split())
car = sorted(list(map(int, input().split())))
expect = []
for i in range(q):
    expect.append([int(input()), 0, i])
expect.sort()
i, j = 0, 0
while i != n and j != q:
    if car[i] == expect[j][0]:
        expect[j][1] = i*(n-i-1)
        j += 1
    elif car[i] >= expect[j][0]:
        j += 1
    else:
        i += 1
        
expect.sort(key=lambda x: x[2])
for i in expect:
    print(i[1])
    