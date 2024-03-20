def f(cnt, b):
    if b > A and b % 2 == 0:
        b //= 2
    elif b > A and str(b)[-1] == '1':
        b = int(str(b)[:-1])
    else:
        if b == A:
            return cnt
        return -1
    return f(cnt+1, b)
            
A, B = map(int, input().split())
print(f(1, B))