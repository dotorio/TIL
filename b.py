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
                while b[y-f] != b[y+f]:
                    if 
            

print(b)

