a = int(input())
b = list(map(int, input().split()))
c = int(input())
for x in range(c):
    d, e = map(int, input().split())
    if d == 1:
        for y in range(a):
            if (y+1) % e == 0:
                if b[y] == 0:
                    b[y] = 1
                else:
                    b[y] = 0
    else:
        for y in range(a):
            for f in range(100):
                if e-f == -1 or e+f == a:
                    break
                if b[e-f-1] == b[e+f-1]:
                    
                    if b[e-f-1] == 1:
                        b[e-f-1] = 0
                        b[e+f-1] = 0
                    else:
                        b[e-f-1] = 1
                        b[e+f-1] = 1
            

print(b)

