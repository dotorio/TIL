w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())
rightleft = t % (2 * w)
updown = t % (2 * h)
right = True
up = True
while rightleft:
    if p == w:
        right = False
    elif p == 0:
        right = True
    if right == True:
        p += 1
        rightleft -= 1
    else:
        p -= 1
        rightleft -= 1
while updown:
    if q == h:
        up = False
    elif q == 0:
        up = True
    if up == True:
        q += 1
        updown -= 1
    else:
        q -= 1
        updown -= 1
print(p, q)