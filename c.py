a, b = map(int, input().split())
c = int(input())
e1 = [0, b]
e2 = [0, a]
l1 = []
l2 = []
area = []
for x in range(c):
    d, e = map(int, input().split())
    if d == 0:
        e1.append(e)
    else:
        e2.append(e)
e1.sort()
e2.sort()
for y in range(len(e1)-1):
    l1.append(e1[y+1]-e1[y])
for z in range(len(e2)-1):
    l2.append(e2[z+1]-e2[z])
for y2 in l1:
    for z2 in l2:
        area.append(y2*z2)
print(max(area))