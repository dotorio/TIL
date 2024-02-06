T = int(input())
for i in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    a = (x1-x2)**2+(y1-y2)**2 
    b = (r1+r2)**2
    c = (r1-r2)**2
    if a == 0 and r1 == r2:
        print(-1)
    elif c == a or b == a:
        print(1)
    elif c < a < b:
        print(2)   
    else:
        print(0)
