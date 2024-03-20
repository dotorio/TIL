import sys
sys.stdin = open('input.txt')

def make_set(n):
    return [i for i in range(n)]

# 1~6번까지 사용하기 위해 7로 만듬
parents = make_set(7)

def find_set(x):
    if parents[x] == x:
        return x
    return find_set(parents[x])

def union(x, y):
    x = find_set(x)
    y = find_set(y)

    if x == y:
        return
    
    if x < y:
        parents[y] = x
    else:
        parents[x] = y

union(1, 3)
union(2, 3)
union(5, 6)
print(parents)